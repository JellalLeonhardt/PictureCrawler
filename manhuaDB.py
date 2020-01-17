from retrying import retry
from lxml import html
import zipfile
import base64
import json
import time
import sys
import os
import requests
import urllib
import mylogger


def str2nums(strList):
    '''
    传入str list，返回对应的int list
    支持的str：单个数字 范围（数字-数字）
    '''
    nums = []
    for s in strList:
        s = str(s)
        if '-' in s:
            r = s.split('-')
            start = int(r[0])
            end = int(r[1])
            for i in range(start, end + 1):
                nums.append(i)
        else:
            nums.append(int(s))

    return nums


def compressZip(sourcePath, targetPath):
    '''
    :param sourcePath:待压缩文件所在文件目录
    :param targetPath:目标文件
    :return:null
    '''

    tarZip = zipfile.ZipFile(targetPath, 'w', zipfile.ZIP_STORED)
    fileList = []
    for root, dirs, files in os.walk(sourcePath):
        for file in files:
            fileList.append(os.path.join(root, file))

    for filename in fileList:
        tarZip.write(filename, filename[len(sourcePath):])
    tarZip.close()


@retry(wait_random_min=100, wait_random_max=400, stop_max_attempt_number=3)
def getHTML(url, sleep=0.2):
    content = requests.get(url).content.decode()
    time.sleep(sleep)
    return html.fromstring(content)


@retry(wait_random_min=100, wait_random_max=400, stop_max_attempt_number=3)
def writePicture(url, filepath, sleep=0.2, headers={}):
    time_start = time.time()
    with open(filepath, "wb") as jpg:
        jpg.write(requests.get(url, headers=headers).content)
    time_end = time.time()
    time.sleep(sleep)
    mylogger.info(filepath, time_end-time_start, 's')


def downloadPicture(url, filepath, sleep=0.2, headers={}):
    if os.path.exists(filepath):
        mylogger.info('skip', filepath)
        return
    try:
        writePicture(url, filepath, sleep, headers)
    except Exception as e:
        os.remove(filepath)
        mylogger.error('error skip', filepath)


if __name__ == '__main__':
    # url = str(input("url:"))
    url = "https://www.manhuadb.com/manhua/162"
    downloadDir = 'D:\\manga\\OnePunch'
    target = getHTML(url)
    lists = target.xpath('//li[@class="sort_div fixed-wd-num"]') + \
        target.xpath('//li[@class="sort_div "]')
    names = target.xpath('//li[@class="sort_div fixed-wd-num"]/a/text()') + \
        target.xpath('//li[@class="sort_div "]/a/text()')
    picurls = target.xpath('//li[@class="sort_div fixed-wd-num"]/a/@href') + \
        target.xpath('//li[@class="sort_div "]/a/@href')
    errorSkips = ''
    for i in range(0, len(lists)):
        print(i, names[i])

    nums = input("输入要下载的序号：")
    nums = nums.split(" ")
    nums = str2nums(nums)
    for i in range(0, len(lists)):  # 遍历所有章节/卷
        if i not in nums:
            continue
        firstPage = 'https://www.manhuadb.com' + picurls[i]
        print('start downloading', names[i], firstPage)
        subDir = os.path.join(downloadDir, names[i])
        if not os.path.exists(subDir):
            os.makedirs(subDir)

        try:
            subtarget = getHTML(firstPage)
        except Exception as e:
            errorSkips += firstPage + '\t' + str(i) + '\n'
            print('error skip', i, firstPage)
            continue

        # 可以从第一页拿到图片所在的host和prefix
        host = subtarget.xpath(
            '//div[@class="d-none vg-r-data"]/@data-host')[0]
        pre = subtarget.xpath(
            '//div[@class="d-none vg-r-data"]/@data-img_pre')[0]
        scripts = subtarget.xpath('//script/text()')
        imagedata = ''  # 可以从第一页中拿到所有的图片数据（base64加密后的json）
        for script in scripts:
            if 'img_data' in script:
                imagedata = script.replace(
                    'var img_data = \'', '').replace('\';', '')

        images = json.loads(str(base64.b64decode(imagedata), "utf-8"))
        for img in images:  # 遍历json数组拿到图片页数("p")和具体地址("img")
            imgPath = subDir + "\\" + str(img["p"]) + ".jpg "
            if os.path.exists(imgPath):
                print('skip', imgPath)
                continue
            imgURL = host + pre + img["img"]  # 组装host prefix img 得到完整地址
            try:
                writePicture(imgURL, imgPath)
            except Exception as e:
                os.remove(imgPath)
                errorSkips += imgURL + '\t' + str(i) + '\n'
                print('error skip', i, imgURL)

        compressZip(subDir, subDir + ".zip")

    print('error skips', errorSkips)

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

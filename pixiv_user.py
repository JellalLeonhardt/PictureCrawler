import urllib2
import requests
import os
import time
import json
import gzip
import StringIO
from lxml import html
nums = []
nums = list(map(int, raw_input().split()))
# while 1:
#    try:
#        s = raw_input()
#        nums.append(s)
#    except:
#        break
cookie = input("cookie:")
send_headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.pixiv.net/member_illust.php?id=340628',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
send_headers['cookie'] = cookie
for num in nums:
    url = 'https://www.pixiv.net/ajax/user/{}/profile/all'.format(num)
    req = urllib2.Request(url, headers=send_headers)
    try:
        r = urllib2.urlopen(req)
    except Exception as e:
        print('Error:', e)
        break
    source = r.read()
    compressedstream = StringIO.StringIO(source)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    source = gziper.read()
    source = source.decode('utf-8')
    images_json = json.loads(source)
    for image in images_json['body']['illusts']:
        url_target = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id={}'.format(
            image)
        req_target = urllib2.Request(url_target, headers=send_headers)
        r_target = urllib2.urlopen(req_target)
        target_target = gzip.GzipFile(fileobj=StringIO.StringIO(
            r_target.read())).read().decode('utf-8')
        first = target_target.find("img-original")
        second = target_target.find("\"", first)
        final_url = 'https:\/\/i.pximg.net/' + target_target[first:second]
        final_url = final_url.replace('\\/', '/')
        print(final_url)
        name_start = final_url.rfind('/')
        name = '/home/pixiv_pictures/' + final_url[name_start + 1:]
        picture = urllib2.urlopen(urllib2.Request(
            final_url, headers=send_headers))
        with open(name, "wb") as jpg:
            jpg.write(picture.read())
    print('finishi!', num)

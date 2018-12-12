import urllib2
import requests
import os
import time
import json
from lxml import html
a = int(input("start:"))
b = int(input("end:"))
cookie = input("cookie:")
send_headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': cookie,
    'pragma': 'no-cache',
    'referer': 'https://www.pixiv.net/member_illust.php?id=340628',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
for num in range(a, b + 1, 1):
    url = 'https://www.pixiv.net/ajax/user/{}/profile/all'.format(num)
    req = urllib2.Request(url, headers=send_headers)
    try:
        r = urllib2.urlopen(req)
    except Exception as e:
        print('Error:', e)
        break
    source = r.read()
    images_json = json.loads(source)
    for image in images_json['body']['illusts']:
        print image
    exit()
    target = html.fromstring(source.decode('utf-8'))
    titles = target.xpath('//a[@class="sc-hSdWYo NeoCZ"]/text()')
    purls = target.xpath('//a[@class="sc-hSdWYo NeoCZ"]/@href')
    for picture in titles, purls:
        fname = '/home/pixiv_pictures/' + picture[0] + '.jpg'
        url_target = 'https://www.pixiv.net' + picture[1]
        req_target = urllib2.Request(url_target, headers=send_headers)
        r_target = urllib2.urlopen(req_target)
        target_target = html.fromstring(r_target.read().decode('utf-8'))
        first = target_target.find("img-original")
        second = target_target.find("\"", first)
        print source[first:second]
        send_headers['Referer'] = 'https://www.pixiv.net' + picture[1]
        # with open(name, "wb") as jpg:
        #    jpg.write(requests.get(picture[1]).content)
    print('finishi!', num)

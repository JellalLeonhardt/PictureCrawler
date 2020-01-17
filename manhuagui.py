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
import utils
import mylogger

if __name__ == '__main__':
    urlFmt = 'https://i.hamreus.com/ps3/y/yiquanchaoren/vol_19/{0:03d}.jpg.webp?cid=465855&md5=p8imqiLi0DQPzWGC-oKKcg'
    referer = 'https://www.manhuagui.com/comic/7580/465855.html'
    downloadDir = 'D:\\manga\\OnePunch\\19'
    if not os.path.exists(downloadDir):
        os.makedirs(downloadDir)

    for i in range(1, 228):
        url = urlFmt.format(i)
        mylogger.info(url)
        path = os.path.join(downloadDir, '{}.jpg'.format(i))
        utils.downloadPicture(url, path, headers={
            'Referer': referer})

    utils.compressZip(downloadDir, downloadDir+'.zip')

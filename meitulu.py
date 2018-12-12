import urllib2
import requests
import os
import time
from lxml import html
a = int(input("start:"))
b = int(input("end:"))
send_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'
}
for num in range(a, b + 1, 1):
    url = 'http://mtl.ttsqgs.com/images/img/' + '{}/'.format(num)
    img = 0
    send_headers['Referer'] = 'https://www.meitulu.com/item/{}.html'.format(num)
    req = urllib2.Request(send_headers['Referer'], headers=send_headers)
    r = urllib2.urlopen(req)
    source = r.read()
    target = html.fromstring(source.decode('utf-8'))
    title = target.xpath('//div[@class="weizhi"]/h1/text()')[0]
    fname = '/home/pictures/' + title
    os.makedirs(fname)
    while 1:
        img = img + 1
        img_url = url + '{}.jpg'.format(img)
	print img_url
        req = urllib2.Request(img_url, headers=send_headers)
        try:
            r = urllib2.urlopen(req)
            name = fname + '/{}.jpg'.format(img)
    	    with open(name, "wb") as jpg:
            	jpg.write(r.read())
        except Exception as e:
            print('Error:', e)
            break
    print('finishi!', num)

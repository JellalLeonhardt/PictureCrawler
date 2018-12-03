import urllib2
import requests
import os
import time
from lxml import html
year = 2015
page = 1
os.makedirs('{}'.format(page))
while 1:
    i=1
    d = 0
    url = 'http://fm.shiyunjj.com/{}'.format(year) + '/{}'.format(page) + '/{}.jpg'.format(i)
    send_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive'
    }
    print url
    req = urllib2.Request(url, headers=send_headers)
    try:
        r = urllib2.urlopen(req)
	if r.getcode() == 404:
            if i == 1:
		print '+1y'
		year = year + 1
		i=1
		continue
	    print '+1p'
	    page = page + 1
	    i=1
	    os.makedirs('{}'.format(page))
	    continue
	r.close()
        fname = '/home/pictures/{}'.format(page) + '/{}.jpg'.format(img)
        with open(fname, "wb") as jpg:
            jpg.write(requests.get(url).content)
    except Exception as e:
        print('Error:', e)

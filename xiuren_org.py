import urllib2
import requests
import os
import time
from lxml import html
section = input("target:")
a = int(input("start:"))
b = int(input("end:"))
send_headers = {
    'Host': 'www.meizitu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}
for num in range(a, b + 1, 1):
	url = 'http://www.xiuren.org/' + section + '-{0:03d}.html'.format(num)
	req = urllib2.Request(url, headers=send_headers)
	r = urllib2.urlopen(req)
    source = r.read()
	if r.getcode() == 404:
		break
    title = html.fromstring(source.decode('utf-8')).xpath('//div[@id="title"]/h1/text()')
    print title
    d = 0
    url = 'http://www.xiuren.org/' + section + '/{0:03d}/'.format(num)
	fname = '/home/pictures/' + title
    os.makedirs(fname)
    while 1:
		d = d + 1
		url = url + '{0:04d}.jpg'.format(d)
        print url
        name = fname+('/{0:04d}.jpg'.format(d))
        print name
		try:
			with open(name, "wb") as jpg:
				jpg.write(requests.get(c).content)
				time.sleep(0.1)
   		except Exception as e:
        	print('Error:', e)
			break
    print('finishi!', num)

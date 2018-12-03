import urllib2
import requests
import os
import time
from lxml import html
section = raw_input("target:")
a = int(input("start:"))
b = int(input("end:"))
send_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}
for num in range(a, b + 1, 1):
    url = 'http://www.xiuren.org/' + section + '-{0:03d}.html'.format(num)
    req = urllib2.Request(url, headers=send_headers)
    try:
    	r = urllib2.urlopen(req)
    except Exception as e:
	print('Error:', e)
	break
    source = r.read()
    target = html.fromstring(source.decode('utf-8'))
    title = target.xpath('//div[@id="title"]/h1/text()')[0]
    print title
    purl = target.xpath('//span[@class="photoThum"]/a/@href')
    fname = '/home/pictures/' + title
    os.makedirs(fname)
    d = 0
    for jpg_url in purl:
	print jpg_url
	d = d + 1
        name = fname+('/{0:04d}.jpg'.format(d))
        with open(name, "wb") as jpg:
            jpg.write(requests.get(jpg_url).content)
    print('finishi!', num)

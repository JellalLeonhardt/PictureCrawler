import urllib2
import requests
import os
import time
from lxml import html
a = int(input("start:"))
b = int(input("end:"))
for num in range(a, b, 1):
    d = 0
    url = 'http://www.meizitu.com/a/{}.html'.format(num)
    send_headers = {
    	'Host':'www.meizitu.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Connection':'keep-alive'
    }
    print url
    req = urllib2.Request(url, headers = send_headers)
    r = urllib2.urlopen(req)
    source = r.read()
    source = source.decode('gbk')
    target = html.fromstring(source)
    lists = target.xpath('//div[@class="metaRight"]/h2/a/text()')
    if len(lists)==0:
        continue
    title = target.xpath('//div[@class="metaRight"]/h2/a/text()')[0]
    print title
    purl = target.xpath('//div[@id="picture"]/p/img/@src')
    fname = '/home/pictures/' + title
    print fname
    os.makedirs(fname)
    for c in purl:
        print c
        d = d+1
        name = fname+('/{}.jpg'.format(d))
        print name
        with open(name, "wb") as jpg:
            jpg.write(requests.get(c).content)
            time.sleep(0.1)
    print('finishi!', num)

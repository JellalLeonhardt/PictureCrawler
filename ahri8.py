import urllib2
import requests
import os
import time
from lxml import html
url = "https://ahri8.com/"
page = "readOnline2.php?ID=38975&host_id=0&page=1"
while 1:
    current = url + page
    req = urllib2.Request(current, headers=send_headers)
    try:
        r = urllib2.urlopen(req)
        source = r.read()
        source = source.decode('gbk')
        target = html.fromstring(source)
        next_page = title = target.xpath(
            '//a[@onclick="return goNextPage();"]/text()')[0]
        if page == next_page:
            break
        title = target.xpath('//h1[@class="page-header"]/text()')[0]
        print title
        purl = target.xpath('//div[@id="show_image_area"]/div/img/@src')
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
    except Exception as e:
        print('Error:', e)

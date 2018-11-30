import urllib
import requests
import os
import time
from lxml import html
a=int(input("start:"))
b=int(input("end:"))
for num in range(a,b,1):
    d=0
    url='http://www.meizitu.com/a/{}.html'.format(num)
    print(url)
    target=html.fromstring(requests.get(url).content)
    title=target.xpath('//div[@class="metaRight"]/h2/a/text()')[0]
    print(title)
    purl=target.xpath('//div[@id="picture"]/p/img/@src')
    fname='D:\\pictures\\' + title
    print(fname)
    os.makedirs(fname)
    for c in purl:
        print(c)
        d=d+1
        name=fname+('\\{}.jpg'.format(d))
        print(name)
        with open(name,"wb") as jpg:
                jpg.write(requests.get(c).content)
                time.sleep(0.1)
    print ('finishi!',num)

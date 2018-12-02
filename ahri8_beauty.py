import urllib2
import requests
import os
import time
import json
from lxml import html
start = input("start:")
end = input("end:")
url = "https://mlgb.today/"
for id in range (start, end + 1):
    page = 'index.php?route=gallery/readOnline&gallery_id==' + str(id) + '&host_id=0&page=1'
    current = url + page
    req = urllib2.Request(current)
    try:
        r = urllib2.urlopen(req)
        source = r.read()
        #source = source.decode('utf-8')
        first = source.find("var HTTP_IMAGE")
        first = source.find("\"", first)
        second = source.find("\"", first + 1)
        image_server = source[first + 1:second]
	first = source.find("Origin", second + 1)
	first = source.find("Origin", first + 1)
	first = source.find("[", first + 1)
	second = source.find("]", first + 1);
	image_source = json.loads(source[first:second + 1])
	images = []
	for image in image_source:
	    images.append(image_server + str(image[u'new_filename'] + '_w900' + '.' + 'jpg')) #no idea where w900 come from
	#print images
        target = html.fromstring(source)
        #next_page = title = target.xpath(
        #    '//a[@onclick="return goNextPage();"]/text()')[0]
        #if page == next_page:
        #    break
        title = target.xpath('//h1[@class="page-header"]/text()')[0]
        #print title
        #purl = target.xpath('//div[@id="show_image_area"]/div/img/@src')
        fname = '/home/pictures/' + title
        print fname
        os.makedirs(fname)
	d = 0
        for i in images:
            d = d+1
            name = fname + ('/{}.'.format(d)) + 'jpg'
            print i
            with open(name, "wb") as jpg:
                jpg.write(requests.get(i).content)
                time.sleep(0.1)
        print('finishi!')
    except Exception as e:
        print('Error:', e)


import urllib2
import re

url = "http://www.quebeccitygasprices.com/"

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    #print response.read()

    content = response.read().decode("utf-8")
    price_pattern = r'<div class="price_num" style="margin-left:12px">(.*?)</div>'


    place_pattern_1 = r'<dl class="address">(.*?)</dl>'



    price_items = re.findall(price_pattern, content, re.S|re.M)
    for i in price_items:
        print i


    place_pattern_2 = re.findall(place_pattern_1, content, re.S|re.M)
    for line in place_pattern_2:
        name_pattern = r'<a .*?>(.*?)</a>'
        name_items = re.findall(name_pattern, line)
        for j in name_items:
            print j
        add_pattern = r'<dd>(.*?)</dd>'
        add_items = re.findall(add_pattern, line)
        for k in add_items:
            print k


except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

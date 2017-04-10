
import urllib2
import re
import HTMLParser
import itertools

url = "http://www.quebeccitygasprices.com/"

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    #print response.read()

    content = response.read().decode("utf-8")

    main_pattern = r'<tr id=.*?>(.*?)</tr>'
    # price_pattern = r'<div class="price_num" style="margin-left:12px">(.*?)</div>'
    # place_pattern_1 = r'<dl class="address">(.*?)</dl>'
    main_items = re.findall(main_pattern, content, re.S|re.M)

    for line in main_items:
        pr_pattern = r'<div class="price_num" .*?">(.*?)</div>'
        pr_items = re.findall(pr_pattern, line)
#        for i in pr_items:
#            print i

        name_pattern = r'<a .*? onclick=.*?>(.*?)</a>'
        name_items = re.findall(name_pattern, line)
 #       for j in name_items:
#            print j

        add_pattern = r'<dd>(.*?)</dd>'
        add_items = re.findall(add_pattern, line)
#        for k in add_items:
#            print HTMLParser.HTMLParser().unescape(k)

        for i, j, k, in itertools.izip(pr_items, name_items, add_items):
            print i, j, HTMLParser.HTMLParser().unescape(k)

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

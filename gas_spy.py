
import urllib2
import re
import HTMLParser
# import itertools


def getPrice():
    global pr_items, name_items, add_items

    url = "http://www.quebeccitygasprices.com/"

    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)

        content = response.read().decode("utf-8")

        main_pattern = r'<tr id="rrlow_0".*?>(.*?)</tr>'

        main_items = re.findall(main_pattern, content, re.S | re.M)

        for line in main_items:
            # Find the price value
            pr_pattern = r'<div class="price_num" .*?">(.*?)</div>'
            pr_items = re.findall(pr_pattern, line)

            # Find the name of gas station
            name_pattern = r'<a .*? onclick=.*?>(.*?)</a>'
            name_items = re.findall(name_pattern, line)

            # Find the address
            add_pattern = r'<dd>(.*?)</dd>'
            add_items = re.findall(add_pattern, line)

        return pr_items, name_items, add_items
#        for i, j, k, in itertools.izip(pr_items, name_items, add_items):
#            print i, j, HTMLParser.HTMLParser().unescape(k)

    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason


def sendResult():
    return "The lowest price of gas now is $"+ pr_items[0] + " at " + name_items[0] +"\nIts address is " + HTMLParser.HTMLParser().unescape(add_items[0])


if __name__ == '__main__':

    getPrice()
    print sendResult()

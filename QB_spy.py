import urllib2
# import requests
import re
# import html       # for remove &amp in string
import time


def getQB():
    global joke_items, name_items, add_items

    url = "https://www.qiushibaike.com/"

    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    try:
        #request = requests.get(url, headers=headers)
        #content = request.text
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)

        content = response.read().decode("utf-8")

        main_pattern = r'<div class="article block untagged mb15".*?title=".*?">.*?<div class="content">(.*?)</div>'

        main_items = re.findall(main_pattern, content, re.S)

        # for line in main_items:
        #     # Find the price value
        #     joke_pattern = r'<div class="price_num" .*?">(.*?)</div>'
        #     joke_items = re.findall(joke_pattern, line)

        #     # Find the name of gas station
        #     name_pattern = r'<a .*? onclick=.*?>(.*?)</a>'
        #     name_items = re.findall(name_pattern, line)

        #     # Find the address
        #     add_pattern = r'<dd>(.*?)</dd>'
        #     add_items = re.findall(add_pattern, line)

        msg = main_items

        print(msg[0])
        return msg

    #except requests.HTTPError as e:
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


if __name__ == '__main__':

    print(getQB())

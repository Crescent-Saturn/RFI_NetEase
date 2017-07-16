
import requests
import re
import html       # for remove &amp in string
import time
import random


def getPrice():
    global pr_items, name_items, add_items

    url = "http://www.quebeccitygasprices.com/"

    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    user_agent = random.choice(agents)
    headers = {'User-Agent': user_agent}

    try:
        request = requests.get(url, headers=headers)
        content = request.text

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

        msg = "The lowest gas price now (" + time.ctime() + ") is $%s" % pr_items[0] + " at " + name_items[0]

        if name_items[0] != 'Costco':
            msg = msg + "\nIts address is " + html.unescape(add_items[0])

        # print(msg)
        return msg

    except requests.HTTPError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


if __name__ == '__main__':

    print(getPrice())

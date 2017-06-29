
import requests
import re
import html       # for remove &amp in string
import sched
import time

from wxpy import *

def getPrice(action_time):
    global pr_items, name_items, add_items

    url = "http://www.quebeccitygasprices.com/"

    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    try:
        request = requests.get(url, headers=headers)
        content = request.text

        # content = response.read().decode("utf-8")

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

        #return pr_items, name_items, add_items
#        for i, j, k, in itertools.izip(pr_items, name_items, add_items):
#            print i, j, HTMLParser.HTMLParser().unescape(k)
        msg = "The lowest price of gas now (" + time.strftime("%c")+") is $%s" % pr_items[0] + " at " + name_items[0]
        # ads = "\nIts address is " + html.unescape(add_items[0])

        if name_items[0] != 'Costco':
            msg = msg + "\nIts address is " + html.unescape(add_items[0])
        scheduler.enterabs(action_time + 5, 1, getPrice, (action_time + 5,))

        print(msg)
        bot.self.send(msg)
        # return msg

    except requests.HTTPError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


# def sendResult():
#     return "The lowest price of gas now is $" + pr_items[0] + " at " + name_items[0] +"\nIts address is " + HTMLParser.HTMLParser().unescape(add_items[0])


if __name__ == '__main__':

    bot = Bot()
    init_time = time.time()
    scheduler = sched.scheduler(time.time, time.sleep)

#    print getPrice(init_time)
    scheduler.enterabs(init_time, 1, getPrice, (init_time,))
    scheduler.run()

#    print sendResult()

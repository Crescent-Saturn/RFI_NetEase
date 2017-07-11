import requests
import re
import random


def getQB():
    global joke_items, name_items, add_items

    url = "https://www.qiushibaike.com/"

    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    try:
        request = requests.get(url, headers=headers)
        content = request.text

        main_pattern = r'<span>(.*?)</span>'

        main_items = re.findall(main_pattern, content, re.S)



        msg = random.choice(main_items)

        print(msg)
        return msg

    except requests.HTTPError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


if __name__ == '__main__':

    getQB()

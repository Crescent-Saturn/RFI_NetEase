import requests
import re
import random
import codecs


def getQB():
    global joke_items, name_items, add_items

    url = "https://www.qiushibaike.com/"

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

        main_pattern = r'<div class="content">(.*?)</div>'

        main_items = re.findall(main_pattern, content, re.S)
        # print(main_items)
        # for line in main_items:
            # item_pattern = r'<span>(.*?)</span>'
            # items = re.findall(item_pattern, line, re.S|re.M)
        with codecs.open('file_done.txt', 'a+', 'utf-8') as f:
            for item in main_items:
                Img = re.search("img", item)
                if Img:
                    del item
                item.strip()
                if not len(item):
                    continue
                f.write(item)

        return main_items

    except requests.HTTPError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


if __name__ == '__main__':

    print(getQB())

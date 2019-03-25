import pyautogui as ag
import time
import random

ag.PAUSE = 0.1
ag.FAILSAFE = True

w, h = ag.size()
# pyautogui.click()
# x, y = pyautogui.position()


def initial_click():
    global h, w
    ag.click(x=w / 3, y=h / 15)

    ag.click()
    ag.doubleClick()
    ag.click()
    ag.typewrite('bing.com', 0.05)
    ag.press('tab')
    ag.typewrite('Google', 0.05)
    ag.press('enter')
    time.sleep(1.5)
    # ag.click(x=800, y=500)
    # time.sleep(0.5)
    # ag.press('enter')


def auto_bing(words):
    global h, w
    ag.click(x=w / 3, y=h / 5)

    ag.click()
    ag.doubleClick()

    ag.typewrite(words, 0.1)
    ag.press('enter')
    time.sleep(0.8)

# ag.typewrite('bing.com', 0.15)
# ag.press('tab')
# ag.typewrite('new from python!', 0.15)
# ag.press('enter')


if __name__ == '__main__':
    initial_click()
    # ag.click(x=w / 3, y=h / 5)
    # words = "Bing is a web search engine owned and operated by Microsoft. The service has its origins in Microsoft's previous search engines: MSN Search, Windows Live Search and later Live Search. Bing provides a variety of search services, including web, video, image and map search products. Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. "
    # for word in words.split():
    for word in range(31):
        auto_bing(str(word))

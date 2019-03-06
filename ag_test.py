import pyautogui as ag
import time

ag.PAUSE = 0.1
ag.FAILSAFE = True

# pyautogui.click()
# x, y = pyautogui.position()


def initial_click():
    ag.click(x=800, y=100)

    ag.click()
    ag.doubleClick()
    ag.click()
    ag.typewrite('bing.com', 0.02)
    ag.press('enter')
    ag.click(x=800, y=500)
    time.sleep(0.5)
    ag.press('enter')


def auto_bing(words):
    ag.click(x=800, y=270)

    ag.click()
    ag.doubleClick()

    ag.typewrite(words, 0.05)
    ag.press('enter')

# ag.typewrite('bing.com', 0.15)
# ag.press('tab')
# ag.typewrite('new from python!', 0.15)
# ag.press('enter')


if __name__ == '__main__':
    initial_click()
    words = "Bing is a web search engine owned and operated by Microsoft. The service has its origins in Microsoft's previous search engines: MSN Search, Windows Live Search and later Live Search. Bing provides a variety of search services, including web, video, image and map search products."
    for word in words.split():
        auto_bing(word)

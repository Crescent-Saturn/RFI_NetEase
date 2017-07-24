import schedule
import time
import random
import codecs
from pyquery import PyQuery
from wxpy import *

from QB_spy_py3 import getQB
import get_gas_price

global my_friend_2, my_friend_1, fr_list


def get_price():
    price = get_gas_price.getPrice()
    bot.self.send(price)
    print(price)


def send_QB():
    list_items = get_QB_item()
    item_f = random.choice(list_items)
    doc = PyQuery(item_f)
    my_friend_1.send(doc.text())

    fr_done = random.choice(fr_list)
    my_friend_2 = bot.friends().search(fr_done)[0]
    my_friend_2.send(doc.text())
    # print(doc.text())

    list_items.remove(item_f)
    with codecs.open('file_done.txt', 'w', 'utf-8') as fg:
        for i in list_items:
            fg.write(i + '\n')


def get_QB_item():
    list_items = []
    with codecs.open('file_done.txt', 'r', 'utf-8') as f:
        lines = f.readlines()
        for item in lines:
            item = item.strip()
            if not len(item):
                continue
            list_items.append(item)
        return list_items




bot = Bot()


@bot.register(Friend)
def auto_reply(msg):
    if 7 <= msg.receive_time.hour < 23:
        return
    else:
        return u'【自动回复】(' + str(msg.create_time) +u') 收到消息：{}({})'.format(msg, msg.type) + u'\n不出意外的情况下我应该在睡觉，请理解！醒来后回复~'

# schedule.every(0.1).minutes.do(get_price)


# send_QB()
# get_price()
schedule.every(6).hours.do(get_price)
schedule.every().day.at("10:00").do(send_QB)
schedule.every().sunday.do(getQB)
# print(get_gas_price.getPrice())

while True:
    schedule.run_pending()
    time.sleep(1)

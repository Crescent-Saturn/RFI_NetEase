import schedule
import time
from wxpy import *

import get_gas_price


def get_price():
    price = get_gas_price.getPrice()
    bot.self.send(price)
    print(price)


bot = Bot()
# my_friend = bot.friends().search(u'')[0]


@bot.register()
def auto_reply(msg):
    # print(u'【自动回复】(' + str(msg.create_time) +') 收到消息)')
    if 7 <= msg.receive_time.hour < 23:
        msg.forward(bot.self, prefix='From: {}'.format(msg.sender))
    else:
        return u'【自动回复】(' + str(msg.create_time) +') 收到消息：{}'.format(msg, msg.type) + u'\n不出意外的情况下我应该在睡觉，请理解！醒来后回复~'

# embed()

schedule.every(6).hours.do(get_price)
print(get_gas_price.getPrice())

while True:
    schedule.run_pending()
    time.sleep(1)

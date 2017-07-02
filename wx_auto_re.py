import schedule
import time
from wxpy import *

import get_gas_price


def send_msg():
    msg = get_gas_price.getPrice()
    bot.self.send(msg)
    # my_friend.send(u'这是一条自动发送测试消息，如果收到请告知我，谢谢！')


bot = Bot()
my_friend = bot.friends().search(u'')[0]
schedule.every(0.1).minutes.do(send_msg)

while True:
    schedule.run_pending()
    time.sleep(1)

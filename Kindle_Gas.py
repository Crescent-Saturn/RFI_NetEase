from get_kindle import kindle_now
from gas_spy import getPrice
import schedule
import time
from sendSMS import sms2me


def update():
    msg = getPrice()
    sms2me(msg)
# print(msg)


def KPW():
    msg = kindle_now()
    # msg = 'The Kindle Paperwhite now is $' + str(price)
    sms2me(msg)


# print('The Kindle Paperwhite now is $' + str(price))
# assert float(price) < 100, "It's not time, wait for it!"


# schedule.every(3).hours.do(getPrice)
schedule.every().day.at("9:00").do(update)

# schedule.every().monday.do(KPW)
schedule.every().monday.at("10:00").do(KPW)

update()
# time.sleep(1)
# KPW()
while True:
    schedule.run_pending()
    time.sleep(1)

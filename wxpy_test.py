from wxpy import *
import random
import time

OkWords = []
with open('blessings.txt', 'r') as f:
    lines = f.readlines()
    for item in lines:
        item = item.strip()
        if not len(item):
            continue
        OkWords.append(item)

# msg = random.choice(OkWords)
bot = Bot(cache_path=True)

fr_list = bot.friends()


# me = fr_list[0]

# print(fr_list)

for friend in new_list:
    msg = random.choice(OkWords)
    friend.send(f'祝愿{friend.name}和家人，' + msg)
    time.sleep(.2)

# print(my_friends.stats_text())

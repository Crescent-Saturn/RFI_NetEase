# -*- coding: UTF-8 -*-
import os, random#, time
from QB_spy import getQB
import codecs

os.chdir('V:\\Usagers\lelei\Desktop\Learning\Py')

# with codecs.open('file_test.txt', 'wb', 'utf-8') as f:
#     main_items = getQB()
#     for i in main_items:
#         f.write(i)
items = []
with open('file_test.txt', 'r') as f:
    lines = f.readlines()
    for item in lines:
        item = item.strip()
        #print item,
        if not len(item):           # find whether this line is empty
            continue
        items.append(item)

print random.choice(items)

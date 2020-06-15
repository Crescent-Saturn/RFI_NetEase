"""
Small web crawling for downloading French daily sentence
"""
import requests
from datetime import date
import sys
from requests_html import HTMLSession


def get_content(url, filename):
    with open(filename, 'wb') as f:
        r = requests.get(url)
        f.write(r.content)
        print(f'{filename} has been downloaded successfully!')


# main url
url_base = 'https://www.frdic.com/home/dailysentence'

session = HTMLSession()

r = session.get(url_base)

# define audio names by today
ds_date = date.today().strftime("%Y%m%d")
normal = ds_date[-4:] + '.mp3'
slow = ds_date[-4:] + '_slow.mp3'

# find sentence first
sentence = r.html.find('#getLang', first=True)

txt = ds_date[-4:] + '.md'

# save into txt
with open(txt, 'w') as f:
    f.write(sentence.text.replace('\n','\\\r'))
    print(f'Daily-sentence texts have been saved in {txt}.')

# find daily photo link
# photo = r.html.find('#showerimg',first=True)
#photo_link = photo.element.attrib['src']

# find audios
audio_normal = r.html.find('#normal-play', first=True)
audio_slow = r.html.find('#slow-play', first=True)

audio_normal_link = audio_normal.element.attrib['data']
audio_slow_link = audio_slow.element.attrib['data']

# start downloading...
#get_content(photo_link, photo_link[-10:])

# print(audio_normal_link)
# print(audio_slow_link)

#r = requests.get(audio_slow_link)
# print(r)
get_content(audio_normal_link, normal)

get_content(audio_slow_link, slow)

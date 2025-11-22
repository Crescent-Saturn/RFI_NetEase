"""
Small web crawling for downloading French daily sentence
"""

import requests
from datetime import date
# import sys
from requests_html import HTMLSession


def get_content(url, filename):
    with open(filename, "wb") as f:
        r = requests.get(url, headers=headers)
        f.write(r.content)
        print(f"{filename} has been downloaded successfully!")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.174 Safari/537.36"
}

# main url
url_base = "https://www.frdic.com/home/dailysentence"

session = HTMLSession()

r = session.get(url_base)

# define audio names by today
ds_date = date.today().strftime("%Y%m%d")

txt = ds_date + ".md"
normal = ds_date + ".mp3"
slow = ds_date + "_slow.mp3"

# find sentence first
main_sentence = r.html.find("#senten_move", first=True)
exp_sentence = r.html.find(".an-info.info_fr", first=True)

exp_text = exp_sentence.text
idx = exp_text.find("\n\n.eg {color")
exp_text = exp_text[:idx]

word = exp_sentence.find(".eg", first=True).text

# post processing
main_text = main_sentence.text.replace("\n", "\\\n> ")
main_text = "> " + main_text
exp_text = exp_text.replace("\n", "\n\n")

# the final format will be "word + main text and explanation"
md_output = word + "\n\n" + main_text + "\n\n" + exp_text

# save into txt
with open(txt, "w") as f:
    f.write(md_output)
    print(f"Daily-sentence texts have been saved in {txt}.")

# find daily photo link
# photo = r.html.find('#showerimg',first=True)
# photo_link = photo.element.attrib['src']

# find audios
audio_normal = r.html.find("#normal-play", first=True)
audio_slow = r.html.find("#slow-play", first=True)

audio_normal_link = audio_normal.element.attrib["data"]
audio_slow_link = audio_slow.element.attrib["data"]

# start downloading...
# get_content(photo_link, photo_link[-10:])

# print(audio_normal_link)
# print(audio_slow_link)

# r = requests.get(audio_slow_link)
# print(r)
get_content(audio_normal_link, normal)

get_content(audio_slow_link, slow)

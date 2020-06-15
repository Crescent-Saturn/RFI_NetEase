import requests
from requests_html import HTMLSession
from datetime import date
import sys

url_base = 'http://aod-rfi.akamaized.net/rfi/francais/audio/jff/'
# https://aod-rfi.akamaized.net/rfi/francais/audio/jff/202004/journal_francais_facile_journal_en_francais_facile_20200406.mp3

# url_spe = 'http://telechargement.rfi.fr/savoirs/apprendre/actu/jff/jff_'

# url_tg = 'http://telechargement.rfi.fr/rfi/francais/audio/jff/201812/journal_francais_facile_20h00_-_20h10_tu_20181231.mp3'
# dt = datetime.now()
# print(dt.strftime("%Y%m%d"))

txt_base = 'https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-francaise/journal-en-francais-facile-'  # -20h00-gmt'
# https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-francaise/journal-en-francais-facile-13062020-20h00-gmt

# url_time_m = dt.strftime("%Y%m")
# url_time_d = dt.strftime("%Y%m%d")

if len(sys.argv) > 1:
    url_date = sys.argv[1]
else:
    url_date = date.today().strftime("%Y%m%d")

url_month = url_date[:-2]
# url_news = 'journal_francais_facile_20h00_-_20h10_tu_'
url_news = 'journal_francais_facile_journal_en_francais_facile_'

# fileName = url_news + url_month + '.mp3'
fileName = ''.join([url_news, url_date, '.mp3'])

# fileName_new = url_date[-2:] + url_date[-4:-2] + url_date[:4] + '.mp3'
# fileName_new = ''.join([url_date[-2:], url_date[-4:-2], url_date[:4], '.mp3'])

# url_tg = url_base + url_time_m + '/' + fileName
url_tg = ''.join([url_base, url_month, '/', fileName])

# print(url_tg)
# print(fileName)

saveName = ''.join([url_date, '.mp3'])
saveName = fileName.replace(url_news, '')
# print(saveName)

# final txt url
txt_url = txt_base + url_date[-2:] + \
    url_date[-4:-2] + url_date[:4] + '-20h00-gmt'
# print(txt_url)

txt_name = url_date + '.md'

# Debug
# txt_url = 'https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-francaise/journal-en-francais-facile-11062020-20h00-gmt'
# print(txt_url)

r = HTMLSession().get(txt_url)
# print(r.status_code)

# find full texts
txt = r.html.find('#content-area', first=True)

# change into md file type
final_txt = txt.text.replace('\n', '\n\n')

# Saving full text
print('Saving full text into md file...')
if r.status_code == 200:
    with open(txt_name, 'w') as f:
        f.write(final_txt)
    print(f'{url_date}.md has been written to the disk!')
else:
    print(
        f'ERROR! The text file cannot be accessed because of {r.status_code}, please try later.')


# Downloading audio file
r = requests.get(url_tg)

# REMOVE
# if r.status_code == 404:
#     url_tg = ''.join([url_spe, fileName_new])
#     # print(url_tg)
#     r = requests.get(url_tg)

print('Downloading audio file...')

if r.status_code == 200:
    with open(fileName.replace(url_news, ''), 'wb') as code:
        code.write(r.content)
    print(f'{url_date}.mp3 has been downloaded to the disk!')
else:
    print(
        f'ERROR! The mp3 file cannot be accessed because of {r.status_code}, please try later.')

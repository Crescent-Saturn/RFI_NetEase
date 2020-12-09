import requests
from requests_html import HTMLSession
from datetime import date
import sys

# url_base = 'http://aod-rfi.akamaized.net/rfi/francais/audio/jff/'
url_base = 'https://aod-rfi.akamaized.net/rfi/francais/audio/jff/'  
# https://aod-rfi.akamaized.net/rfi/francais/audio/jff/202004/journal_francais_facile_journal_en_francais_facile_20200406.mp3

# url_spe = 'http://telechargement.rfi.fr/savoirs/apprendre/actu/jff/jff_'
url_spe = "https://aod-rfi.akamaized.net/savoirs/apprendre/actu/jff/jff-" #15082020.mp3"
# 'https://aod-rfi.akamaized.net/rfi/francais/audio/jff/202012/journal_francais_facile_20h00_-_20h10_gmt_20201204.mp3'

txt_base = 'https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-francaise/journal-en-francais-facile-'  # -20h00-gmt'
# https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-francaise/journal-en-francais-facile-13062020-20h00-gmt



def get_context(txt_url, date):
    r = HTMLSession().get(txt_url)
    # print(r.status_code)

    # find full texts
    txt = r.html.find('#content-area', first=True)

    # change into md file type
    final_txt = txt.text.replace('\n', '\n\n')

    # Saving full text
    print('\nSaving full text into md file...')
    if r.status_code == 200:
        with open(f'{date}.md', 'w') as f:
            f.write(final_txt)
        print(f'{date}.md has been written to the disk!')
    else:
        print(
            f'ERROR! The text file cannot be accessed because of {r.status_code}, please try later.')



def get_audio(url_target, date):
    # Downloading audio file
    r = requests.get(url_target)

    # REMOVE
    if r.status_code == 404:
        fileName_new = day + month + year + '.mp3'

        url_target = url_spe + fileName_new

        r = requests.get(url_target)

    print('\nDownloading audio file...')

    if r.status_code == 200:
        with open(f'{date}.mp3', 'wb') as code:
            code.write(r.content)
        print(f'{date}.mp3 has been downloaded to the disk!')
    else:
        print(
            f'ERROR! The mp3 file cannot be accessed because of {r.status_code}, please try later.')


def get_context_url(date):
    url_context = txt_base + day + month + year + '-20h00-gmt'
    return url_context


def get_audio_url(date):
    
    url_audio = url_base + year + month + '/' + url_news + date + '.mp3'
    return url_audio


if len(sys.argv) > 1:
    url_date = sys.argv[1:]
else:
    url_date = date.today().strftime("%Y%m%d")

for date in url_date:
    # get year, month and day
    year = date[:4]
    month = date[-4:-2]
    day = date[-2:]

    # url_news = 'journal_francais_facile_20h00_-_20h10_tu_'
    # url_news = 'journal_francais_facile_journal_en_francais_facile_'
    url_news = 'journal_francais_facile_20h00_-_20h10_gmt_'

    # get audio file
    url_audio = get_audio_url(date)
    get_audio(url_audio, date)

    # get context
    url_context = get_context_url(date)
    get_context(url_context, date)

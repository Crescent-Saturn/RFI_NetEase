import requests
from datetime import datetime

url_base = 'http://telechargement.rfi.fr/rfi/francais/audio/jff/'

# url_tg = 'http://telechargement.rfi.fr/rfi/francais/audio/jff/201812/journal_francais_facile_20h00_-_20h10_tu_20181231.mp3'
dt = datetime.now()
# print(dt.strftime("%Y%m%d"))


url_time_m = dt.strftime("%Y%m")
url_time_d = dt.strftime("%Y%m%d")
url_news = 'journal_francais_facile_20h00_-_20h10_tu_'

fileName = url_news + url_time_d + '.mp3'

url_tg = url_base + url_time_m + '/' + fileName

print(url_tg)
print(fileName)

r = requests.get(url_tg)
with open(fileName, 'wb') as code:
    code.write(r.content)

import requests
from datetime import date
import sys

url_base = 'http://telechargement.rfi.fr/rfi/francais/audio/jff/'
# url_spe = 'http://telechargement.rfi.fr/savoirs/apprendre/actu/jff/jff_19022019.mp3'
url_spe = 'http://telechargement.rfi.fr/savoirs/apprendre/actu/jff/jff_'
 
# url_tg = 'http://telechargement.rfi.fr/rfi/francais/audio/jff/201812/journal_francais_facile_20h00_-_20h10_tu_20181231.mp3'
# dt = datetime.now()
# print(dt.strftime("%Y%m%d"))


# url_time_m = dt.strftime("%Y%m")
# url_time_d = dt.strftime("%Y%m%d")

if len(sys.argv) > 1:
    url_date = sys.argv[1]
else:
    url_date = date.today().strftime("%Y%m%d")
	
url_month = url_date[:-2]
url_news = 'journal_francais_facile_20h00_-_20h10_tu_'

# fileName = url_news + url_month + '.mp3'
fileName = ''.join([url_news,url_date,'.mp3'])

# fileName_new = url_date[-2:] + url_date[-4:-2] + url_date[:4] + '.mp3'
fileName_new = ''.join([url_date[-2:], url_date[-4:-2], url_date[:4], '.mp3'])

# url_tg = url_base + url_time_m + '/' + fileName
url_tg = ''.join([url_base,url_month,'/',fileName])

# print(url_tg)
# print(fileName)

# saveName = ''.join([url_date,'.mp3'])
# saveName = fileName.replace(url_news,'')
# print(saveName)


r = requests.get(url_tg)

if r.status_code == 404:
    url_tg = ''.join([url_spe, fileName_new])
    # print(url_tg)
    r = requests.get(url_tg)



# print(r.status_code)
with open(fileName.replace(url_news,''), 'wb') as code:
    code.write(r.content)

# print(f'{saveName} has been downloaded to the disk!')
print('New mp3 has been downloaded to the disk!')

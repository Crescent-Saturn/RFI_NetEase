import requests as np
# import urllib
# import urllib2

url = 'https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-fran%C3%A7aise/journal-en-fran%C3%A7ais-facile'

rfi_ul = 'http://telechargement.rfi.fr/rfi/francais/audio/jff/201703/journal_francais_facile_20h00_-_20h10_tu_20170307.mp3'

r = np.get(rfi_ul)


with open('code.mp3','wb') as code:
    code.write(r.content)
# print(type(r))
# print(r.status_code)
# print(r.encoding)
# print(r.text)
# print(r.content)

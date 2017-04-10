
import os
import urllib2

os.chdir('V:\\Usagers\lelei\Desktop\Learning')
print os.getcwd()

rfi_ul = 'http://telechargement.rfi.fr/rfi/francais/audio/jff/201704/journal_francais_facile_20h00_-_20h10_tu_20170409.mp3'

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

request = urllib2.urlopen(rfi_ul)
r = request.read()

with open('test.mp3','wb') as code:
    code.write(r)

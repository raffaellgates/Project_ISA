
import re
from bs4 import BeautifulSoup
import requests

global fist
fist = [1]
global historico
historico = []


def search(keyword, url, depth, new):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')
    links = soup.find_all('a')
    html = soup.find_all(text=True)

    text = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
    ]

    for t in html:
        if t.parent.name not in blacklist:
            text += '{} '.format(t)

    urls_normais = []

    for link in links:
        try:
            # tratando urls
            url_re = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', str(link['href']))

            if str(link['href'])[0] == '/':
                url_re = url + url_re
                urls_normais.append(str(link['href'])[1:])
            elif len(url_re) > 0:
                urls_normais.append(url_re[0])

        except Exception:
            continue

    else:
        search_key = ('.'*20) + keyword + ('.'*20)
        ocorrencias = re.findall(search_key, text, re.IGNORECASE)
        i = len(ocorrencias)
        if i > 0:
        	print("%s, %d resultados" %(url,i))
        	historico.append([i, url, keyword])
        if depth > 0:
            depth -= 1
            quantidade_link = len(urls_normais)
            for i in range(quantidade_link):
                try:
                	search(keyword=keyword, url=urls_normais[i], depth=depth, new=True)
                except Exception:
                    continue




# search('coronavírus', 'http://brasil.gov.br', 2, True)
search('PI', 'http://www.ifpi.edu.br', 1, True)
historico.sort(reverse=True) 
db.executemany('INSERT INTO urls VALUES (?,?,?)', historico)
connection.commit()
connection.close()

#test
print('-------------resultados-------------')
for i in range(len(historico)):
    print('%iº - %s - %i encontradas'%(i+1,historico[i][1],historico[i][0]))

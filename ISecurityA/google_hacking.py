import re
from bs4 import BeautifulSoup
import requests
from search import search_links

all_link = []


def main():
    url = "https://www.facebook.com/"
    search = search_links(url)
    for s in search:
        google_hacking(s)
    for i in all_link:
        print("-" + i[0])
    print(f"quantidade de links encontrados: {len(all_link)}")


def google_hacking(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')
    links = soup.find_all("a")

    for link in links:
        try:
            # tratando urls
            url_re = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', str(link['href']))
            if len(url_re) > 0:
                all_link.append(url_re)
            # if str(link['href'])[0] == '/':
            #     url_re = url + url_re
            #     urls_normais.append(str(link['href'])[1:])
            # elif len(url_re) > 0:
            #     urls_normais.append(url_re[0])
        except Exception:
            continue


main()

import re
from bs4 import BeautifulSoup
import requests
from .search import (
    search_links,
    filter_link,
    ignore_link
    )

all_link = []


def analisar(url):
    ignore_link(url)
    search = search_links(url)
    for s in search:
        google_hacking(s)
    filter_link(all_link, url)
    # for i in links:
    #     print(i[0])
    # print(f"quantidade de links encontrados: {len(links)}")       


def google_hacking(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')
    links = soup.find_all("a")
    # print(len(links))

    for link in links:
        try:
            url_re = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', str(link['href']))
            if len(url_re) > 0:
                all_link.append(url_re)
        except Exception:
            continue

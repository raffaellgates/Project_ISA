from bs4 import BeautifulSoup
import requests
import re
from .models import DadosSensiveis, Search
searchs = []
VULNERABILIDADE_XSS = []
VULNERABILIDADE_SQL_INJECTION = []
DOCS_FOUND = []
DADOS_SENSIVEIS = []


def search_links(url):
    # theharvester()
    caminho = url.split("/")[2]
    hostname = caminho.split('.')[0]
    dominio = caminho.split('.')[1]
    tld = caminho.split('.')[2]
    links_hostname(hostname)
    links_dominio(dominio)
    links_tld(tld)
    return searchs


def links_hostname(hostname):
    pass


LINK_DOMINIO = [
    "/search?q=site%3A+dominio.com+filitype%3A+txt",
    "/search?q=site%3A+dominio.com+filitype%3A+pdf",
    "/search?q=site%3A+dominio.com+filitype%3A+sql",
    "/search?q=site%3A+dominio.com+filitype%3A+png",
    "/search?q=site%3A+dominio.com+filitype%3A+txt+intext%3A+'password'",
    "/search?q=site%3A+dominio.com+filitype%3A+txt+intext%3A+'users'",
    "/search?q=site%3A+dominio.com+intext%3A+'user'",
    "/search?q=site%3A+dominio.com+intext%3A+'password'",
    "/search?q=site%3A+dominio.com+intext%3A+'email'",
    "/search?q=site%3A+dominio.com+intext%3A+'data'",
    "/search?q=site%3A+dominio.com+intext%3A+'senha'",
    "/search?q=site%3A+dominio.com+intext%3A+'login'",
    "/search?q=site%3A+dominio.com+intext%3A+'hacking'",
    "/search?q=site%3A+dominio.com+intitle%3A+'user'",
    "/search?q=site%3A+dominio.com+intitle%3A+'password'",
    "/search?q=site%3A+dominio.com+intitle%3A+'email'",
    "/search?q=site%3A+dominio.com+intitle%3A+'data'",
    "/search?q=site%3A+dominio.com+intitle%3A+'senha'",
    "/search?q=site%3A+dominio.com+intitle%3A+'login'",
    "/search?q=site%3A+dominio.com+inurl%3A+'senha'",
    "/search?q=site%3A+dominio.com+inurl%3A+'login'",
    "/search?q=site%3A+dominio.com+intitle%3A+'hacking'",
    "/search?q=site%3A+dominio.com+inurl%3A+/wp-content'",
    "/search?q=site%3A+dominio.com+inurl%3A+/wp-admin'",
    "/search?q=site%3A+dominio.com+inurl%3A+/adm",
    "/search?q=site%3A+dominio.com+inurl%3A+/wp-admin",
    "/search?q=site%3A+dominio.com+inurl%3A+.com/search.asp",
    "/search?q=site%3A+dominio.com+inurl%3A+.asp",
    "/search?q=site%3A+dominio.com+inurl%3A+php?",
    "/search?q=site%3A+dominio.com+inurl%3A+.php?",



]
IGNORE_LINK = [
    "https://support.google.com/websearch%3Fp%3Dws_settings_location%26hl%3Dpt-BR",
    "https://accounts.google.com/ServiceLogin%3Fcontinue%3Dhttps",
    "https://www.google.com/preferences?hl=pt-BR",
    "https://policies.google.com/privacy?hl=pt-BR",
    "https://policies.google.com/terms?hl=pt-BR",
    "https://www.google.com/",
    "https://www.google.de/",
    "https://maps.google.com/maps?q=/search%3Fq%3Dsite",
    "https://www.google.com/preferences%3Fhl%3Dpt-BR",
    "https://www.google.com/search?ie=UTF-8",
    "https://www.google.com/imgres?imgurl=https"

]


def ignore_link(url):
    IGNORE_LINK.append(url)
    not_www(url)


def not_http(url):
    pass


def not_www(url):
    dominio = url.split('.')
    if dominio == 'https://www':
        link = url.split('/')[2].split('w.')[1]
        IGNORE_LINK.append(link)


def filter_link(links, url):
    list = []
    try:
        for link in links:
            if ((link[0] in IGNORE_LINK)):
                continue
            else:
                list.append(link)
                IGNORE_LINK.append(link[0])
    except Exception:
        pass
    verificar_link(list, url)


def links_dominio(dominio):
    for link in LINK_DOMINIO:
        link1 = link.split('dominio')[0]
        link2 = link.split('dominio')[1]
        google = "https://www.google.com"
        link_for_search = f"{google}{link1}{dominio}{link2}"

        searchs.append(link_for_search)


def links_tld(tls):
    pass


def verificar_link(links, url):
    separar_links_por_vulnerabilidades(links, url)
    explorar_dados(url)


def separar_links_por_vulnerabilidades(links, url):
    for link in links:
        if ('pdf' in link[0] or 'txt' in link[0]):
            DOCS_FOUND.append(link[0])
        elif ('sql' in link[0] or 'xml' in link[0]):
            DOCS_FOUND.append(link[0])
        elif ('asp' in link[0]):
            VULNERABILIDADE_XSS.append(link[0])
        elif ('php?' in link[0]):
            VULNERABILIDADE_SQL_INJECTION.append(link[0])
        else:
            DADOS_SENSIVEIS.append(link[0])
    print(DADOS_SENSIVEIS)
    vulnerabilidade_xss(url)
    vulnerabilidade_SQL_injection(url)
    docs_found(url)


def vulnerabilidade_xss(url):
    for link in VULNERABILIDADE_XSS:
        try:
            response = requests.get(link, timeout=20)
            if response.status_code == 404:
                soup = BeautifulSoup(response.text, 'html5lib')
                input = soup.find_all("input")
                if len(input) > 0:
                    pass
                    add_SGBD(link, url, 3)
        except Exception:
            add_SGBD(link, url, 3)
            continue


def vulnerabilidade_SQL_injection(url):
    for link in VULNERABILIDADE_SQL_INJECTION:
        try:
            test = link + "'"
            response = requests.get(test, timeout=20)
            soup = BeautifulSoup(response.text, 'html5lib')
            keyword = 'SQL'
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
                # there may be more elements you don't want, such as "style", etc.
            ]

            for t in html:
                if t.parent.name not in blacklist:
                    text += '{} '.format(t)

            ocorrencias = re.findall(keyword, text, re.IGNORECASE)
            i = len(ocorrencias)
            if i > 0:
                pass
                add_SGBD(link, url, 3)
        except Exception:
            add_SGBD(link, url, 3)
            continue


def docs_found(url):
    for link in DOCS_FOUND:
        add_SGBD(link, url, 4)


def explorar_dados(url):
    for link in DADOS_SENSIVEIS:
        try:
            response = requests.get(link, timeout=20)
            if (response.status_code != 404):
                soup = BeautifulSoup(response.text, 'html5lib')
                keyword = verificar_caminho(url)
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

                ocorrencias = re.findall(keyword, text, re.IGNORECASE)
                i = len(ocorrencias)
                if i > 0:
                    add_SGBD(link, url, 1)
                    print('ok dd')
            else:
                continue
        except Exception:
            continue


def verificar_caminho(url):
    caminho = url.split('/')[2].split('.')
    if len(caminho) == 3:
        return caminho[1]
    elif len(caminho) > 4 and caminho[0] == 'www':
        return caminho[1]
    elif len(caminho) > 3 and caminho[3] != '.com':
        return caminho[1]
    else:
        return caminho[0]


def add_SGBD(link, url, tipo):
    if Search.objects.filter(url=url).exists():
        search = Search.objects.get(url=url)
        obj = DadosSensiveis(
            link=link,
            tipo_vulnerabilidade=tipo,
            url_primary_id=search)
        obj.save()
    else:
        new_search = Search(url=url)
        new_search.save()
        obj = DadosSensiveis(
            link=link,
            url_primary_id=new_search,
            tipo_vulnerabilidade=tipo
            )
        obj.save()

searchs = []


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
    # "/search?q=site%3A+dominio.com+filitype%3A+txt",
    # "/search?q=site%3A+dominio.com+filitype%3A+pdf",
    # "/search?q=site%3A+dominio.com+filitype%3A+png",
    # "/search?q=site%3A+dominio.com+filitype%3A+txt+intext%3A+'password'",
    # "/search?q=site%3A+dominio.com+filitype%3A+txt+intext%3A+'users'",
    # "/search?q=site%3A+dominio.com+intext%3A+'user'",
    # "/search?q=site%3A+dominio.com+intext%3A+'password'",
    # "/search?q=site%3A+dominio.com+intext%3A+'email'",
    # "/search?q=site%3A+dominio.com+intext%3A+'data'",
    # "/search?q=site%3A+dominio.com+intext%3A+'senha'",
    # "/search?q=site%3A+dominio.com+intext%3A+'login'",
    # "/search?q=site%3A+dominio.com+intext%3A+'hacking'",
    # "/search?q=site%3A+dominio.com+intitle%3A+'user'",
    # "/search?q=site%3A+dominio.com+intitle%3A+'password'",
    # "/search?q=site%3A+dominio.com+intitle%3A+'email'",
    # "/search?q=site%3A+dominio.com+intitle%3A+'data'",
    # "/search?q=site%3A+dominio.com+intitle%3A+'senha'",
    # "/search?q=site%3A+dominio.com+intitle%3A+'login'",
    # "/search?q=site%3A+dominio.com+intitle%3A+'hacking'",
    # "/search?q=site%3A+dominio.com+inurl%3A+/wp-admin'",
    # "/search?q=site%3A+dominio.com+inurl%3A+/adm",
    "/search?q=site%3A+dominio.com+inurl%3A+/wp-admin"


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
    return list


def links_dominio(dominio):
    for link in LINK_DOMINIO:
        link1 = link.split('dominio')[0]
        link2 = link.split('dominio')[1]
        google = "https://www.google.com/search?q="
        link_for_search = f"{google}{link1}{dominio}{link2}"

        searchs.append(link_for_search)


def links_tld(tls):
    pass


def verificar_link(links):
    outros = separar_links_por_vulnerabilidades(links)
    faz_algo(outros)


def separar_links_por_vulnerabilidades(links):
    outros = []
    return outros


def faz_algo(links):
    pass

searchs = []


def search_links(url):
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
    "/search?q=site%3A+dominio.com",
    "/search?q=site%3A+dominio.com+filitype%3A+txt",
    "/search?q=site%3A+dominio.com+filitype%3A+pdf",
    "/search?q=site%3A+dominio.com+filitype%3A+png",

]


def links_dominio(dominio):
    for link in LINK_DOMINIO:
        link1 = link.split('dominio')[0]
        link2 = link.split('dominio')[1]
        google = "https://www.google.com/search?q="
        link_for_search = f"{google}{link1}{dominio}{link2}"

        searchs.append(link_for_search)


def links_tld(tls):
    pass

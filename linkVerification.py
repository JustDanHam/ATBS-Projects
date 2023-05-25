#! python3
# linkVerification.py - checks all links on a web page, and notifies of
# any broken links.

import requests
import bs4


def linkVeri(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select('a')
    for linkElem in linkElems:
        link = linkElem.get('href')
        if str(link).startswith('https://'):
            res = requests.get(link)
            try:
                res.raise_for_status()
                print(f'Link found: {link}')
            except Exception as exc:
                print(f'There was a problem with the url: {exc}')

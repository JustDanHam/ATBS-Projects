#! python3
# swcd.py (scheduledWebComicDownloader) - checks several web comics and downloads
# if comic was updated since last visit.

import os
import requests
import bs4


folderName = 'webComics'
os.makedirs(folderName, exist_ok=True)

def findNewComic(comicUrl):
    filename = os.path.basename(comicUrl)

    if filename in os.listdir(folderName):
        print(f'No new comic found. Most recent comic ({comicUrl}) has already been downloaded.')
        return

    print(f'Downloading new comic: {comicUrl}')

    res = requests.get(comicUrl)
    res.raise_for_status()
    imageFile = open(os.path.join(folderName, filename), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

def getXkcd():
    siteUrl = 'https://xkcd.com'

    res = requests.get(siteUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')

    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        findNewComic(comicUrl)

def getExplosm():
    siteUrl = 'https://explosm.net'

    res = requests.get(siteUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic-short img')

    if comicElem == []:
        print('Could not find comic image.')

    else:
        comicUrl = comicElem[0].get('src')
        findNewComic(comicUrl)


getXkcd()
getExplosm()


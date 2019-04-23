import requests
import requests_cache
from bs4 import BeautifulSoup
from IPython.display import Image
import pandas as pd
requests_cache.install_cache("bases_scraping", expire_after=10e5)



def scrapUrl(url):
    headers = {
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
				"Accept-Encoding": "gzip, deflate, br",
				"Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
				"Cache-Control": "max-age=0",
				"Connection": "keep-alive",
				"Host": "www.leboncoin.fr",
				"Referer": "https://www.google.com/",
				"Upgrade-Insecure-Requests": '1',
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

			}
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, "lxml")


def fillTable(all_ads,list_all_ads):
    for ads in all_ads:
        try:
            temps = ads.find("p",class_="mAnae").get_text()
        except:
            temps = None
        try:
            price = ads.find("span",class_="_1NfL7").get_text()  #prix
        except:
            price = None
        try:
            title = ads.find(itemprop="name").get_text()  #prix
        except:
            title = None
        list_all_ads.append({"title":title, "price":price, "temps": temps})
    return list_all_ads
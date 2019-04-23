
from IPython.display import Image
from bs4 import BeautifulSoup
import requests_cache
import pandas as pd
import datetime

requests_cache.install_cache("bases_scraping", expire_after=10e5)

from scrappingTools import scrapUrl,fillTable

from dataTraiting import FindBonneAffaire
import sendMail

def run():
    f= open("logs.txt","w+")
    url = "https://www.leboncoin.fr/recherche/?category=15&text=thinkpad&locations=r_12"+"&page="
    page=0
    unFind=None
    list_all_ads = []
    while unFind==None:
        page += 1
        try:
            soup = scrapUrl(url+str(page))
            all_ads = soup.find("ul",class_="undefined").find_all("li")
            list_all_ads=fillTable(all_ads,list_all_ads)
        except:
            unFind=soup.find("p",class_="_2fdgs")

    f.write(str(datetime.datetime.now()))
    f.write("\n  #"+page)
    df_leboncoin = pd.DataFrame(list_all_ads).dropna(how = 'any')

    offres=FindBonneAffaire(df_leboncoin)
    sendMail.send(offres)
    f.write("\n Email sent successfully")



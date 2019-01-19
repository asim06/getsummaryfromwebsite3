import requests
from bs4 import BeautifulSoup


#Read News Application


#
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})




print("Lütfen bekleyin... Haberler çekiliyor...\n")
url= "http://ekonomi.haber7.com/"
istek=requests.get(url,headers)
icerik=istek.content
soup = BeautifulSoup(icerik, "html.parser")


print(" LİNKlER VE  HABERLER ŞU ŞEKİLDE:\n ------------------------------")

#Learn News Name and Link From Website
haberler=soup.find_all("div",{"class": "title"})
linkler=soup.find_all("a",{"class": "news"})

sayi=1 # we use count for news
for i in haberler:

    print(sayi, "-)", i.text)
    sayi+=1

sayi =1
for i in linkler:

    print(sayi, "-)", i.get("href"))
    sayi+=1
    istek2 = requests.get(i.get("href"), headers)
    istek_soup = BeautifulSoup(istek2.content, "lxml")
    print(istek2.status_code, "İstek durumu")
    metin = istek_soup.find_all("div", {"class": "news-content"})
    for j in metin:
        print(j.text)





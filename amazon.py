import requests
from urllib import request
from bs4 import BeautifulSoup
from urllib.request import Request


url = "https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/dp/B09G9D8KRQ/ref=sr_1_1_sspa?crid=3A1UV3VOUPK1R&keywords=iphone&qid=1700540577&sprefix=iphones%2Caps%2C565&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
request_site = Request(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
html = request.urlopen(request_site).read()
soup = BeautifulSoup(html,"html.parser")

def iphoneInfo():
    titleobj = soup.find("div", {"class": "centerColAlign"})
    titleobj2 = titleobj.find("h1",{"class": "a-size-large a-spacing-none"})
    title = titleobj2.find("span",{"class":"a-size-large product-title-word-break"}).text
    ratingobj = soup.find("span", {"class": "reviewCountTextLinkedHistogram noUnderline"})
    ratingobj2 = ratingobj.find("span", {"class": "a-declarative"})
    ratingobj3 = ratingobj2.find("a",{"class":"a-popover-trigger a-declarative"})
    rating = ratingobj3.find("span",{"class":"a-size-base a-color-base"}).text
    priceobj = soup.find("div",{"id":"corePriceDisplay_desktop_feature_div"})
    priceobj2 = priceobj.find("div", {"class": "a-section a-spacing-none aok-align-center aok-relative"})
    price =priceobj2.find("span",{"class":"a-price-whole"}).text




    return title,rating,price

title,rating,price = iphoneInfo()
print('title:',title)
print("rating:",rating)
print("price: ",price)
# print(memory)


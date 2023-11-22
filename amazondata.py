from urllib import request
from bs4 import BeautifulSoup
from urllib.request import Request
import json

#url = "https://www.flipkart.com/apple-iphone-14-starlight-128-gb/p/itm3485a56f6e676?pid=MOBGHWFHABH3G73H&lid=LSTMOBGHWFHABH3G73HCNASCL&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=ff3fc605-a5ff-40c4-9305-15ce0f9151e1.MOBGHWFHABH3G73H.SEARCH&ppt=sp&ppn=sp&ssid=4x9q7zqj400000001700537230671&qH=0b3f45b266a97d70"
def soupfunction(url):
    requestsite = Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
    html = request.urlopen(requestsite).read()
    soup = BeautifulSoup(html,"html.parser")
    return soup
def allLinks():
    urls = []
    soup = soupfunction("https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/dp/B09G9D8KRQ/ref=sr_1_1_sspa?crid=3A1UV3VOUPK1R&keywords=iphone&qid=1700540577&sprefix=iphones%2Caps%2C565&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
    iphones = []
    for i in soup.findAll("a"):
        links = i.get("href")
        #urls.append(links)
        if links and links.startswith('/title/tt'):
            full_link = "https://m.imdb.com" + links.strip()
            urls.add(full_link)
        return list(urls)

    def getMobileinfo():
        myData = []
        iphones = allLinks()
        for i in iphones[:15]:
            titleobj = soup.find("div", {"class": "centerColAlign"})
            titleobj2 = titleobj.find("h1", {"class": "a-size-large a-spacing-none"})
            title = titleobj2.find("span", {"class": "a-size-large product-title-word-break"}).text
            ratingobj = soup.find("span", {"class": "reviewCountTextLinkedHistogram noUnderline"})
            ratingobj2 = ratingobj.find("span", {"class": "a-declarative"})
            ratingobj3 = ratingobj2.find("a", {"class": "a-popover-trigger a-declarative"})
            rating = ratingobj3.find("span", {"class": "a-size-base a-color-base"}).text
            priceobj = soup.find("div", {"id": "corePriceDisplay_desktop_feature_div"})
            priceobj2 = priceobj.find("div", {"class": "a-section a-spacing-none aok-align-center aok-relative"})
            price = priceobj2.find("span", {"class": "a-price-whole"}).text

    myData = {
        "Name":title,
        "Rating":rating,
        "Price":price
    }
    myData.append(myData)

    jsonFile = open("finalMovies3.json", "w")
    json.dump(myData, jsonFile)
    # return title,rating,genre,director


if __name__ == "__main_":
    getMobileinfo()




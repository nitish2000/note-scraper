from bs4 import BeautifulSoup
import re
from urlparse import urlparse
import requests
import unicodedata

urls = []


def selectFunction(find, urls):
    for url in urls:
        if "mathsisfun" in url:
            newData = mathsisfun(find)
            if newData!="sorry":
                return newData

        # if "wolfram" in url:
        #     newData = wolfram(find)
        #     if newData!="sorry":
        #         return newData

        else return "sorry, can't find"

def mathsisfun(find):
    
    url = "https://www.mathsisfun.com/sphider/search.php?query="+find+"&type=and&results=1&search=1"
    try: 
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')

        soupGet = soup.get_text()

        if (find in ((unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore')))):
            for link in soup.find_all('a'):
                if "http://" in (link.get('href')):
                    print link.get('href')
                    newData = requests.get(link.get('href')).text
                    soup = BeautifulSoup(newData, 'html.parser')
                    soupGet = soup.find(id = 'content').text
                    newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')
                    while '' in newData:
                        newData.remove('')
                
                    return newData

    except:
        return "sorry"

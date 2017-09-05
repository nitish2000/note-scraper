from bs4 import BeautifulSoup
import re
from urlparse import urlparse
import requests
import unicodedata

def selectFunction(find, urls):
    for url in urls:
        if "mathsisfun" in url:
            newData = mathsisfun(find)
            if newData!="sorry":
                return newData

        if "wikipedia" in url:
            newData = wikipedia(find)
            if newData!="sorry":
                return newData
        
    return urls, ["Couldn't find results for your query anywhere :(", "You might wanna add another website request for scraping :)"]

def mathsisfun(find):
    findit = find.replace(' ', '+')
    
    url = "https://www.mathsisfun.com/sphider/search.php?query="+findit+"&type=or&results=1&search=1"
    
    try: 
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')

        soupGet = soup.get_text()

        if '+' in findit:
            find = findit[0]

        if (find.lower() in ((unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore')).lower())):

            for link in soup.find_all('a'):
                
                if ("http://" in (link.get('href'))) and (".htm" in (link.get('href'))):
                    
                    # print link.get('href')
                    newData = requests.get(link.get('href')).text
                    soup = BeautifulSoup(newData, 'html.parser')
                    soupGet = soup.find(id = 'content').text
                    newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')

                    while '' in newData:
                        newData.remove('')
                                        
                    if not isinstance(newData, list):
                        newData = [newData]

                    return url, newData
                
                else:  
                    print (link)

        return url, ["uh oh, nothing here"]
        

    except:
        return url, ["uh oh, nothing here"]


def wikipedia(find):
    try:
        findit = find.replace(' ', '_')
        url = "https://en.wikipedia.org/wiki/"+findit
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        soupGet = soup.get_text()

        if (find.lower() in ((unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore')).lower())):
            
            soupGet = soup.find(id = 'mw-content-text').text
            newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')

            while '' in newData:
                newData.remove('')
                                
            if not isinstance(newData, list):
                newData = [newData]

            return url, newData

        return url, ["uh oh, nothing here"]

    except:
        return url, ["uh oh, nothing here"]

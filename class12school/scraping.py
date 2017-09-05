from bs4 import BeautifulSoup
import re
from urlparse import urlparse
import requests
import unicodedata
from itertools import combinations

def selectFunction(discover, urls, counter, sub):
    try:
        if sub =="maths":
            if "mathsisfun" in urls[counter]:
                urlx, newData = mathsisfun(discover)
                if newData[0]!="uh oh, nothing here":
                    print (urlx, newData)
                    return urlx, newData
                    
                else:
                    counter+=1
                    return selectFunction(discover, urls, counter, sub)
                    
            else:
                print ("out of math")
                return selectFunction(discover, urls, 0, "general")

        elif ("wikipedia" in urls[counter]) and (counter<len(urls)):
            print ("here")
            urlx, newData = wikipedia(discover)
            print ("there")
            if newData[0]!="uh oh, nothing here":
                print (urlx, newData)
                return urlx, newData

            # else:
            #     print ("in else")
            #     counter+=1
            #     selectFunction(discover, urls, counter, "general")

        elif (counter<len(urls)):
            print ("waiting")
            counter+=1
            return selectFunction(discover, urls, counter, "general")

        raise Exception ('raised')

    except:
        return urls, ["Couldn't discover results for your query anywhere :(", "You might wanna add another website request for scraping :)"]

def mathsisfun(discover):
    discoverit = discover.replace(' ', '+') 
    url = "https://www.mathsisfun.com/sphider/search.php?query="+discoverit+"&type=and&results=1&search=1"
    try: 
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        soupGet = soup.get_text()

        try:
            soupResult = soup.find(id = 'results')

            for link in soupResult.find_all('a'):
                
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


        except:
            print("and failed")

        url = "https://www.mathsisfun.com/sphider/search.php?query="+discoverit+"&type=or&results=1&search=1"
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        soupGet = soup.get_text()

        soupResult = soup.find(id = 'results')

        for link in soupResult.find_all('a'):
            
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

        print("or failed")
        return url, ["uh oh, nothing here"]

    except:
        print("all failed")
        return url, ["uh oh, nothing here"]


def wikipedia(discover):
    
    discoverit = discover.replace(' ', '_')
    url = "https://en.wikipedia.org/wiki/"+discoverit

    try:
        try:
            
            r  = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            soupGet = soup.get_text()
            
            if '_' in discoverit:
                discover = discover.split()[0]

            if ("Wikipedia does not have an article with this exact name".lower() in ((unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore')).lower())):
                raise Exception('This is the exception you expect to handle')

            elif (discover.lower() in ((unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore')).lower())):
                
                soupGet = soup.find(id = 'mw-content-text').text
                newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')

                while '' in newData:
                    newData.remove('')
                                    
                if not isinstance(newData, list):
                    newData = [newData]

                return url, newData

            raise Exception('raised')

        except:
            print ("wiki direct don't work")

        if (' ' in discover):
            discover = discover.split()
            for discover in list(combinations(discover, len(discover)-1)):
                
                discoverit = discover.replace(' ', '_')
                url = "https://en.wikipedia.org/wiki/"+discoverit
                r  = requests.get(url)
                data = r.text
                soup = BeautifulSoup(data, 'html.parser')
                soupGet = soup.get_text()
                
                if '_' in discoverit:
                    discover = discover.split()[0]
                if ("Wikipedia does not have an article with this exact name".lower() in ((unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore')).lower())):
                    raise Exception('This is the exception you expect to handle')

                elif (discover.lower() in ((unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore')).lower())):
                    
                    soupGet = soup.find(id = 'mw-content-text').text
                    newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')

                    while '' in newData:
                        newData.remove('')
                                        
                    if not isinstance(newData, list):
                        newData = [newData]

                    return url, newData
            else:
                raise Exception('This is the exception you expect to handle')

    except:
        return url, ["uh oh, nothing here"]

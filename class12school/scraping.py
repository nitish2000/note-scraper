from bs4 import BeautifulSoup
import re
from urlparse import urlparse
import requests
import unicodedata
import itertools

def selectFunction(discover, urls, counter, sub):
    try:
        if sub =="maths":
            if "mathsisfun" in urls[counter]:
                urlx, newData = mathsisfun(discover)
                if newData[0]!="uh oh, nothing here":
                    # print (urlx, newData)
                    return urlx, newData

            # if "mathsisfun" in urls[counter]:
            #     urlx, newData = wolfram(discover)
            #     if newData[0]!="uh oh, nothing here":
            #         print (urlx, newData)
            #         return urlx, newData ...
                    
                else:
                    counter+=1
                    return selectFunction(discover, urls, counter, sub)
                    
            else:

                return selectFunction(discover, urls, 0, "general")

        elif ("wikipedia" in urls[counter]) and (counter<len(urls)):

            urlx, newData = wikipedia(discover)

            if newData[0]!="uh oh, nothing here":

                return urlx, newData

            else:
                print ("in else")
                counter+=1
                selectFunction(discover, urls, counter, "general")

        elif (counter<len(urls)):
            print ("waiting")
            counter+=1
            return selectFunction(discover, urls, counter, "general")

        raise Exception ('raised')

    except:
        return urls, ["Couldn't discover results for your query anywhere :(", "You might wanna add another website request for scraping :)"]

def mathsisfun(discover):
    discoverit = discover.replace(' ', '+').replace('\'s', '').replace('!', '')
    url = "https://www.mathsisfun.com/sphider/search.php?query="+discoverit+"&type=and&results=1&search=1"
    try: 
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        soupGet = ""

        try:
            soupResult = soup.find(id = 'results')

            for link in soupResult.find_all('a'):
                
                if ("http://" in (link.get('href'))) and (".htm" in (link.get('href'))):           
                    # print link.get('href')
                    newData = requests.get(link.get('href')).text
                    soup = BeautifulSoup(newData, 'html.parser')
                    soupGet = soup.find(id = 'content').find_all(['h3', 'em', 'span', 'li', 'h1', 'h2'])

                    newData = ["" if "Example" in unicodedata.normalize('NFKD', item.text).encode('ascii','ignore').lstrip() else unicodedata.normalize('NFKD', item.text).encode('ascii','ignore').lstrip().upper() if item.name == "h1" or item.name == "h2" else "*\t"+unicodedata.normalize('NFKD', item.text).encode('ascii','ignore').lstrip() if item.name == "li" else unicodedata.normalize('NFKD', item.text).encode('ascii','ignore').lstrip() for item in soupGet][:15]
                    # soupGet = ''.join(map(unicode, soupGet))

                    # newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')

                    while '' in newData:
                        newData.remove('')
                                        
                    if not isinstance(newData, list):
                        newData = [newData]

                    return url, newData


        except Exception as e:
            print(e)
            print("and failed")

        url = "https://www.mathsisfun.com/sphider/search.php?query="+discoverit+"&type=or&results=1&search=1"
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        soupGet = ""

        soupResult = soup.find(id = 'results')

        for link in soupResult.find_all('a'):
            
            if ("http://" in (link.get('href'))) and (".htm" in (link.get('href'))):           
                # print link.get('href')
                newData = requests.get(link.get('href')).text
                soup = BeautifulSoup(newData, 'html.parser')
                soupGet = soup.find(id = 'content').find_all(['h3', 'em', 'span', 'li', 'h1', 'h2', 'img'])

                newData = ["" if "Example" in unicodedata.normalize('NFKD', item.text).encode('ascii','ignore').lstrip() else unicodedata.normalize('NFKD', item.text).encode('ascii','ignore').lstrip().upper() if item.name == "h1" or item.name == "h2" else "*\t"+unicodedata.normalize('NFKD', item.text).encode('ascii','ignore').lstrip() if item.name == "li" else unicodedata.normalize('NFKD', item.text).encode('ascii','ignore').lstrip() for item in soupGet][:10]
                # soupGet = ''.join(map(unicode, soupGet))

                # newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')

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

    try:
        
        try:
            discoverit = discover.replace(' ', '+').replace('\'', '%27').replace('!', '%21').replace(',', '%2C')
            url = "https://en.wikipedia.org/w/index.php?title=Special:Search&profile=all&search="+discoverit
            r  = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            soupGet = soup.get_text()
            
            legible = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore')).lower()
            
            if ("Wikipedia does not have an article with this exact name".lower() in legible):
                raise Exception('raised')

            elif ("From Wikipedia, the free encyclopedia".lower() in legible):
                finalData = []
                
                try:
                    table = soup.find_all('table', class_=re.compile('infobox'))[0]
                    result = {}
                    headline = {}
                    for tr in table.find_all('tr'):

                        if tr.find('th'):
                            try:
                                result[tr.find('th').text] = tr.find('td').text
                            except:
                                headline["SUBJECT"] = tr.find('th').text.upper()
                    
                    newData = [a+": "+result[a] for a in result]
                    newData = [a+": "+headline[a] for a in headline] + newData
                    finalData = newData
                
                except Exception as e:
                    print (e)

                soupGet = soup.find("div", class_ = 'mw-parser-output').find("p").text
                if len(soupGet.split(' '))<10:
                     soupGet = soup.find("div", class_ = 'mw-parser-output').text

                newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')

                while '' in newData:
                    newData.remove('')
                                    
                if not isinstance(newData, list):
                    newData = [newData]

                finalData+=newData

                return url, finalData

            else:
                soupGet = soup.find_all("div", class_ = 'mw-search-result-heading')[0]
                link = soupGet.find_all('a')[0]
                
                newData = requests.get("https://en.wikipedia.org"+link.get('href')).text
                soup = BeautifulSoup(newData, 'html.parser')

                finalData = []
                
                try:
                    table = soup.find_all('table', class_=re.compile('infobox'))[0]
                    result = {}
                    headline = {}
                    for tr in table.find_all('tr'):

                        if tr.find('th'):
                            try:
                                result[tr.find('th').text] = tr.find('td').text
                            except:
                                headline["Subject"] = tr.find('th').text
                    
                    newData = [a+": "+result[a] for a in result]
                    newData = ["______________________"] + [a+": "+headline[a] for a in headline] + newData + ["______________________"]
                    finalData = newData
                
                except Exception as e:
                    print (e)

                soupGet = soup.find("div", class_ = 'mw-parser-output').find("p").text
                if len(soupGet.split(' '))<10:
                     soupGet = soup.find("div", class_ = 'mw-parser-output').text
                     
                newData = (unicodedata.normalize('NFKD', soupGet).encode('ascii','ignore').lstrip()).split('\n')

                while '' in newData:
                    newData.remove('')
                                    
                if not isinstance(newData, list):
                    newData = [newData]

                finalData+=newData

                return url, finalData
        except:
            print ("wikipedia failed")

    except:
        return url, ["uh oh, nothing here"]

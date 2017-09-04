from bs4 import BeautifulSoup
import re

import requests

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data, 'html.parser')


def recursiveFinder(soup):
    if "trigonotry" in soup.get_text():
        print soup.get_text()
    # print soup.find_all(re.compile("*trigonometry*"))
    else:
        for link in soup.find_all('a'):
            try:
                recursiveFinder(BeautifulSoup( (requests.get(link.get('href'))).text,'html.parser'))
            except:
                pass



recursiveFinder(soup)
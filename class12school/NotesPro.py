from flask import Flask, render_template
import re, json, requests, urllib2
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/Notescraper')
def Notescraper():
    sub = ["Mathematics", "Physics", "Chemistry", "Computer Science"]
    return render_template("noteHOME.html", subjects = sub)

@app.route('/Mathematics', methods=['GET', 'POST'])
def Mathematics():
    return render_template("searchMath.html")

@app.route('/Physics', methods=['GET', 'POST'])
def Physics():
    return render_template("searchPhys.html")

@app.route('/Chemistry', methods=['GET', 'POST'])
def Chemistry():
    return render_template("searchChem.html")

@app.route('/Computer Science', methods=['GET', 'POST'])
def CompSci():
    return render_template("searchnitish.html")

@app.route('/search', methods = ['GET', 'POST'])
def getResults():
    sites = getSites()
    return render_template("result.html", result=sites)

def getSites():
    # file handling
    f = open("./static/websites.txt", "r")
    lines = f.read().splitlines()
    f.close()
    
    # iterating sites into key/value pairs
    data = []
    l={}
    i=0
    for line in lines:
        if re.search('<*>', line):
            if (i!=0):
                data.append(l)
            i+=1
            l={}
            l['key'] = re.search('<(.*)>', line).group(1)
            l['value'] = []
        elif re.search('http*', line):
            l['value'].append(line[:-1])
    # souping sites by key
    information=[]
    for obj in data:
        print obj
        if (obj["key"] == "maths"):
            for site in obj['value']:
                page = requests.get(site)
                soup = BeautifulSoup(page.content, 'html.parser')
                information.append(str(list(soup.children)))
                print information
        if (obj["key"] == "physics"):
            for site in obj['value']:
                page = requests.get(site)
                soup = BeautifulSoup(page.content, 'html.parser')
                information.append(str(list(soup.children)))
                print information
        # if (obj["key"] == "chemistry"):
        #     for site in obj['value']:
        #         page = requests.get(site)
        #         soup = BeautifulSoup(page.content, 'html.parser')
        #         information.append(str(list(soup.children)))
        #         print information
        # if (obj["key"] == "computer science"):
        #     for site in obj['value']:
        #         page = requests.get(site)
        #         soup = BeautifulSoup(page.content, 'html.parser')
        #         information.append(str(list(soup.children)))
        #         print information
        # if (obj["key"] == "general"):
        #     for site in obj['value']:
        #         page = requests.get(site)
        #         soup = BeautifulSoup(page.content, 'html.parser')
        #         information.append(str(list(soup.children)))
        #         print information
    
    return information
    
def process():
    pass
app.run(debug = True)












































































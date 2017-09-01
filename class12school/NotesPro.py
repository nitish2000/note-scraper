from flask import Flask, render_template
import re

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
    result = []
    f = open("./static/websites.txt", "r")
    lines = f.read().splitlines()
    f.close()
    result.append(''.join(str(e) for e in lines))
    loadSites(result)
    #return sites
def loadSites(sites):
    sites = str(sites)
    re.search('http://.*Y', 'Y', flags=0)
    l = []
    a = sites[0:7]
    l.append(a)
    b = sites[7:152].split('Y')
    l.append(b)
    c = sites[152:161]
    l.append(c)
    d = sites[161:323].split('Y')
    l.append(d)
    e = sites[323:334]
    l.append(e)
    f = sites[334:431].split('Y')
    l.append(f)
    g = sites[431:449]
    l.append(g)
    h = sites[449:533].split('Y')
    l.append(h)
    i = sites[533:542]
    l.append(i)
    j = sites[542:].split('Y')
    l.append(j)

    return render_template("result.html", result = l)
def process():
    pass
app.run(debug = True)












































































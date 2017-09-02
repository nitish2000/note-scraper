from flask import Flask, render_template
import re, json

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
    data = []
    f = open("./static/websites.txt", "r")
    lines = f.read().splitlines()
    f.close()
    l={}
    for line in lines:
        print line
        if re.search('<*>', line):
            data.append(json.dumps(l))
            l={}
            l['key'] = re.search('<(.*)>', line).group(1)
            l['value'] = []
        elif line!="":
            l['value'].append(line[:-1])

    return data


    return render_template("result.html", result = l)
def process():
    pass
app.run(debug = True)












































































from flask import Flask, render_template, request
import re, json, requests, urllib2
from bs4 import BeautifulSoup
import sqlite3 as sql

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
    # adding websites.txt to database
    msg =[]
    for obj in data:
        for site in obj['value']:
            try:
                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO websites (name,link,uid,pw) VALUES (?,?,?,?)",(obj['key'],site,"erm","erm"))
                    con.commit()
                    msg.append("Record successfully added")
            except Exception as e:
                con.rollback()
                msg.append("error in insert operation: "+ str(e))
            finally:
                # return msg
                con.close()

    return render_template("result.html", result=msg)

    

def createTable():
    conn = sql.connect('database.db')
    print "Opened database successfully";

    conn.execute('CREATE TABLE websites (name TEXT, link TEXT UNIQUE, uid TEXT, pw TEXT)')
    print "Table created successfully";

    conn.close()

@app.route('/')
def home():
    try:
        createTable()
    except:
        print ("table exists")
    return render_template('home.html')

@app.route('/listing')
def listing():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from websites")
   
   rows = cur.fetchall(); 
   return render_template("listing.html",rows = rows)

@app.route('/enternew')
def new_website():
   return render_template('websiteAdd.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         link = request.form['link']
         uid = request.form['uid']
         pw = request.form['pw']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO websites (name,link,uid,pw) VALUES (?,?,?,?)",(name,link,uid,pw))
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("resultDB.html",msg = msg)
         con.close()


def process():
    
    pass

app.run(debug = True)
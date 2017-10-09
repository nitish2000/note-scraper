from flask import Flask, render_template, request
import re, json, requests, urllib2
import sqlite3 as sql
from copy import deepcopy
import scraping
import userClass

app = Flask(__name__)

user = userClass.defaultUser()

def changeUser(userNew = user):
    global user
    user = deepcopy(userNew)

def getUser():
    global user
    return user

########################
# VIEW CONTROL METHODS #
########################

@app.route('/Notescraper')
def Notescraper(user=user):
    sub = ["Mathematics", "Physics", "Chemistry", "Computer Science"]
    return render_template("noteHOME.html", subjects = sub)

@app.route('/Mathematics', methods=['GET', 'POST'])
def Mathematics(user=user):
    return render_template("searchMath.html")

@app.route('/Physics', methods=['GET', 'POST'])
def Physics(user=user):
    return render_template("searchPhys.html")

@app.route('/Chemistry', methods=['GET', 'POST'])
def Chemistry(user=user):
    return render_template("searchChem.html")

@app.route('/Computer Science', methods=['GET', 'POST'])
def CompSci(user=user):
    return render_template("searchnitish.html")

@app.route('/getNotes/<sub>', methods = ['GET', 'POST'])
def getNotes(sub, user=user):
    user = getUser()
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    rows = ""

    if (sub.lower()=="general"):
        cur.execute("SELECT * FROM [" +user.table+ "]")
        rows = cur.fetchall()
    else:
        cur.execute("SELECT * FROM [" +user.table+ "] WHERE name=? OR name=?", (sub, "general",))
        rows = cur.fetchall()

    urls= []
    for value in rows:
        urls.append(str(value['link']))
    
    print urls
    
    toFind = str(request.form['searchItem'])

    url, newData = scraping.selectFunction(toFind, urls, 0, sub)    

    return render_template("scrapeResults.html", result = newData, item = toFind, link = url)

@app.route('/search', methods = ['GET', 'POST'])
def getResults(user=user):   
    user = getUser() 
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
        
    data.append(l)

    # adding websites.txt to database
    msg =[]
    for obj in data:
        for site in obj['value']:
            try:
                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO [" +user.table+ "] (name,link,uid,pw) VALUES (?,?,?,?)",(obj['key'],site,"erm","erm"))
                    con.commit()
                    msg.append("Record successfully added")
            except Exception as e:
                con.rollback()
                msg.append("error in insert operation: "+ str(e))
            finally:
                # return msg
                con.close()

    return render_template("result.html", result=msg)


######################### 
# MODEL CONTROL METHODS #
######################### 

@app.before_first_request
def _run_on_start():
    user = getUser()
    createWebsitesTable(user)
    createUserTable()
    print ("started")

def createWebsitesTable(user=user):
    user = getUser()
    try:
        conn = sql.connect('database.db')
        print "Opened database successfully";
        conn.execute('CREATE TABLE IF NOT EXISTS ['+user.table+'](name TEXT, link TEXT PRIMARY KEY, uid TEXT, pw TEXT)')
        print "Table MADE";
        conn.close()
    except Exception as e:
        print (e)


def createUserTable():
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS listOfUsers(usrname TEXT PRIMARY KEY, pword TEXT, tname TEXT)')
            con.commit()
            print "Table EXISTS";
    except Exception as e:
        con.rollback()
        print (e)
    finally:
        con.close()

@app.route('/')
def home(user=user):
    user = getUser()
    usrname = user.userName
    if user.userName == "default":
        usrname = "User"
    return render_template('home.html', usrname = usrname)

@app.route('/listing')
def listing(user=user):
    user = getUser()
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()

    cur.execute("select * from [" +user.table+ "]")
    rowsWebsites = cur.fetchall() 

    cur.execute("select * from listOfUsers")
    rowsUsers = cur.fetchall() 

    return render_template("listing.html",rowsWebsites = rowsWebsites, rowsUsers=rowsUsers, table=user.description())


# WEBSITES TABLE HANDLING #

@app.route('/enternew')
def new_website():
   return render_template('websiteAdd.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    user = getUser()
    if request.method == 'POST':
        try:
            name = request.form['name']
            link = request.form['link']
            uid = request.form['uid']
            pw = request.form['pw']
            
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO [" +user.table+ "] (name,link,uid,pw) VALUES (?,?,?,?)",(name,link,uid,pw))
                
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
      
        finally:
            con.close()
            return render_template("resultDB.html",msg = msg)


# USER TABLE NEW ACCOUNT #

@app.route('/addUser')
def addUser():
   return render_template('userAdd.html', msg="", username ="")

@app.route('/newUser', methods = ['POST', 'GET'])
def newUser(user = user):
    if request.method == 'POST':
        
        if request.form['pword'] != request.form['pwordRepeat']:
            return render_template('userAdd.html', msg = "passwords don't match", username=request.form['usrname'])

        else:
            try:
                userNew = userClass.User()
                userNew.userName = request.form['usrname']
                userNew.password = request.form['pword']
                userNew.table = str(userNew.userName) + "_websites"

                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO listOfUsers (usrname,pword,tname) VALUES (?,?,?)",(userNew.userName,userNew.password,userNew.table))
                    
                    con.commit()
                    msg = "Your account with has been created successfully: "
                    changeUser(userNew)
                    user = getUser()
                    createWebsitesTable(user)
                
            except Exception as e:
                con.rollback()
                msg = str(e)+"\nSorry, this user name is already in use: "
            
            finally:
                
                con.close()
                return render_template("newUser.html", msg = msg, user = user)

# USER TABLE OLD ACCOUNT #

@app.route('/loginPage')
def loginUser():
   return render_template('loginPage.html', msg="", username ="")

@app.route('/loginMsg', methods = ['POST', 'GET'])
def oldUser(user = user):
    if request.method == 'POST':

        try:
            userNew = userClass.User()
            userNew.userName = request.form['usrname']
            userNew.password = request.form['pword']
            userNew.table = str(userNew.userName) + "_websites"

            with sql.connect("database.db") as con:
                con = sql.connect("database.db")
                con.row_factory = sql.Row
                cur = con.cursor()
                statement = "SELECT count(*) FROM listOfUsers WHERE usrname = ? AND pword = ?"
                print statement
                c = cur.execute(statement,(userNew.userName, userNew.password))
                data=cur.fetchone()[0]
                if data!=0:
                    changeUser(userNew)
                    user = getUser()
                    msg = "\nLogged in Successfully: "
                else:
                    msg = "\nSorry, your account does not exist with the details: "
            
        except Exception as e:
            con.rollback()
            msg = str(e)+"Something Went Wrong"
        
        finally:
            con.close()
            return render_template("loginMsg.html", msg = msg, user = user)

@app.route('/logout')
def logout(user=user):
    user = getUser()
    changeUser(userClass.defaultUser())
    return render_template('logout.html', user=user)

def process():
    pass

app.run(debug = True)

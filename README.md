# note-scraper #

## noteHome ##
    the html file for the main webpage in which we have used bootstrap, html, css and jinja.

## NotesPro ##
    the main python flask file 
    (there's a def loadSites funtion which has all that list splitting code. U can remove that as it doesn't work)

## websites ##
    a text file containing the list of websites for different subjects, from where the data will be scraped from the desired    topic. There is a slash Y after each website meaning yes. (Actually it should be changed to yes or no by the program according to the subject. eg: while searching for a topic in maths, the websites for the websites pertaing to other subjects must hav /n for no.

## result.html is a html file to display something after processing ##
    (it won't work properly i think)


## jpeg images and hi.py ##
    contain some code regarding regular expressions. 
    basically it's about pulling websites from the websites text file but it's incomplete


### 1. BeautifulSoup4(bs4) Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. ###
	https://stackoverflow.com/questions/452283/how-can-i-install-the-beautiful-soup-module-on-the-mac
	https://www.crummy.com/software/BeautifulSoup/bs4/doc/
	http://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python
	https://www.dataquest.io/blog/web-scraping-tutorial-python/


### 9. Model–view–controller (MVC) is a software architectural pattern for implementing user interfaces on computers. It divides a given application into three interconnected parts. This is done to separate internal representations of information from the ways information is presented to, and accepted from, the user.The MVC design pattern decouples these major components allowing for efficient code reuse and parallel development.https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller 


### 10. User class: for the user, subject class: for the various subjects, content provider class: for getting the notes, authentication class: for logging into sites like meritnatin, khanacademy, etc. Classes to be implemented in the main python file running on flask framework (NotesPro). http://flask.pocoo.org/docs/0.12/   http://flask.pocoo.org/docs/0.12/views/   https://stackoverflow.com/questions/40460846/using-flask-inside-class     


### 11. SQlite: To make a database containing userid and passwords for websites from which data can be obtained only after logging into them. It's a package (just like bs4 and flask) which needs to be first installed in your IDE. The module can then be imported using an import statement after installation. https://www.tutorialspoint.com/sqlite/sqlite_installation.htm
	http://flask.pocoo.org/docs/0.12/patterns/sqlite3/     https://sqlite.org/quickstart.html      https://www.tutorialspoint.com/flask/flask_sqlite.htm


### 12. class & objects, data file-handling ---  compulsory concepts to be included in the project


13. Jinja2 :

	http://jinja.pocoo.org/docs/2.9/
    https://www.fullstackpython.com/jinja2.html
    https://realpython.com/blog/python/primer-on-jinja-templating/

14. https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
    https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
    http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python  --- file handling
    https://stackoverflow.com/questions/38042632/mvc-the-simplest-example  --- MVC python
    https://stackoverflow.com/questions/68986/whats-a-good-lightweight-python-mvc-framework?rq=1 ---- MVC framework
    U need to use an MVC framework in python. there are many. install the one of your choice
    https://djangobook.com/model-view-controller-design-pattern/
    

# note-scraper
1. noteHome is the html file for the main webpage in which we have used bootstrap, html, css and jinja.








2. searchMaths, searchPhys etc for specific subjects.







3. NotesPro is the main python flask file (there's a def loadSites funtion which has all that list splitting code. U can remove that as it doesn't work)





4. websites is a text file containing the list of websites for different subjects, from where the data will be scraped from the desired topic. There is a slash Y after each website meaning yes. (Actually it should be changed to yes or no by the program according to the subject. eg: while searching for a topic in maths, the websites for the websites pertaing to other subjects must hav /n for no.


5. hey.py is blank


6. result.html is a html file to display something after processing(it won't work properly i think)


7. there are jpeg images and there is hi.py which contains some code regarding regular expressions. basically it's about pulling websites from the websites text file but it's incomplete.



8. BeautifulSoup4(bs4) Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0ahUKEwiusKHojYTWAhWLpo8KHYwSBlwQFggvMAI&url=https%3A%2F%2Fwww.crummy.com%2Fsoftware%2FBeautifulSoup%2Fbs4%2Fdoc%2F&usg=AFQjCNEjTA5uJ8CpiFoBcuUr2OHbIDHSrg



9. Model–view–controller (MVC) is a software architectural pattern for implementing user interfaces on computers. It divides a given application into three interconnected parts. This is done to separate internal representations of information from the ways information is presented to, and accepted from, the user.The MVC design pattern decouples these major components allowing for efficient code reuse and parallel development.https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller


10. User class: for the user, subject class: for the various subjects, content provider class: for getting the notes, authentication class: for logging into sites like meritnatin, khanacademy, etc. Classes to be implemented in the main python file running on flask framework (NotesPro). http://flask.pocoo.org/docs/0.12/   http://flask.pocoo.org/docs/0.12/views/   https://stackoverflow.com/questions/40460846/using-flask-inside-class     


11. SQlite: To make a database containing userid and passwords for websites from which data can be obtained only after logging into them. It's a package (just like bs4) which needs to be installed in your IDE. The module can be imported using an import statement after installation. http://flask.pocoo.org/docs/0.12/patterns/sqlite3/     https://sqlite.org/quickstart.html      https://www.tutorialspoint.com/flask/flask_sqlite.htm


12. class & objects, data file-handling ---  compulsory concepts to be included in the project

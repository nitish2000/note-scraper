from flask import Flask
app = Flask(__name__)
@app.route('/')
def pullWebsites():
    f = open("C:\Users\\nitish_24\PycharmProjects\class12school\static\websites.txt", "r")
    result = f.read().splitlines()
    f.close()
    return result

app.run(debug = True)
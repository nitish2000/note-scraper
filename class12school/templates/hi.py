from flask import Flask
app = Flask(__name__)
@app.route('/hi')
def pullWebsites():
    f = open("../static/websites.txt", "r")
    lines = f.read().splitlines()
    f.close()
    result  = ''.join(str(e) for e in lines)
    return result

app.run(debug = True)

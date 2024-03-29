from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

#@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):
    # return name

    quotes = [ "Good","Great","Nice" ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]

    return render_template(
        'test.html',**locals())

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

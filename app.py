from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    headline = "hello world!"
    return render_template('index.html', headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye world!"
    return render_template('index.html', headline=headline)

@app.route("/David")
def david():
    return "Hello, David!"

@app.route("/new_years")
def new_years():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("new_year.html", new_year=new_year)

@app.route("/<string:name>")
def hello(name):
    headline = name 
    return render_template('index.html', headline=headline)


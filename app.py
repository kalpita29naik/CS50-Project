from flask import Flask, render_template
import requests
import random
import os
from flask_sqlalchemy import SQLAlchemy

#! Application setups
#Todo
app = Flask(__name__)
app.config["DEBUG"] = True

#! Application Routing

#* This is the default route for the application
#Todo
@app.route("/")
def default():
    return render_template("home.html")

#* This is the Log In route
#Todo
@app.route("/logging")
def logging():
    return render_template("logging.html")

#* This is the route to the pomodoro page
#Todo
@app.route("/pomodoro")
def pomodoro():
    return render_template("pomodoro.html")

#* This is the route to the motivational quote page
#Todo
@app.route("/quote")
def quote():
    quote = requests.get("https://type.fit/api/quotes").json()
    quote = quote[random.randint(0,15)]
    QUOTE=quote["text"]
    AUTHOR = quote["author"].split(",")[0]
    return render_template("quote.html",QUOTE= QUOTE, AUTHOR= AUTHOR)

#* This is the route to the todolist page
#Todo   
@app.route("/todolist")
def todolist():
    return render_template("todolist.html")

#* This is the redirect page to the 404 error page
#Todo
@app.errorhandler(404)
def page_not_found(error):
    return render_template("pagenotfound.html"),404

#! Flask intializer
app.run(host="0.0.0.0", port=int("5000"))
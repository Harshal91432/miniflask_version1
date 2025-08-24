"""
Hello world application of Flask

Command - `flask --app main1 run`   RUn in terminal

- HOME URL

https://swapi.dev
http://127.0.0.1:5000


- RELATIVE

/api/films

- ABSOLUTE URL


"""

from flask import Flask


# `Flask` is a class we use to instantiate an application
app = Flask(__name__)   # pass the current module name


# First http GET request
@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


# SECOND http GET request
@app.route("/greeting")
def custom_message():
    return "<h1>Good Morning</h1>"  # h1 header make word bolt
    #return "<p>Good Morning</p>"

# # SECOND http GET request
# @app.route("/greeting")
# def custom_message():
#
#     import requests
#
#     response = requests.get("https://swapi.dev/api/films/1")
#     # store response in DB
#     return "<h1>data has been saved in DB</h1"
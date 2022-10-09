from flask import Flask
from flask import Flask, redirect, url_for
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/test/<info>')
def home(info):
    print(info)
    if "107.99.42." in info:
       sample_dict = {"107.99.42.19":True,
       "107.99.42.20":True,
       "107.99.42.21":False,
       "107.99.42.22":False
               }
       return {info:sample_dict[info]}
    else:
       return "Not a valid system IP"
    #return "Raviteja"

@app.route('/systems')
def systems():
    print("I am came to systems.")
    return redirect(url_for('C:/Users/Avinash/Desktop/python_practice/Raviteja_teaching/107.99.42.01.html'))

app.run(port=8000)
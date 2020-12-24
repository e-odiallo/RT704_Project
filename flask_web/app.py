#!/usr/bin/python3
#flask_web/app.py
from flask import Flask,render_template, request
import datetime
app = Flask(__name__)

@app.route('/')
def login_page ():
    return render_template("index.html")

@app.route('/result',methods = ['POST'])
def result_page ():
    result = request.form 
    name = result["nom"]
    lastname = result["prenom"]
    return render_template('result.html',nom = name, prenom = lastname)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



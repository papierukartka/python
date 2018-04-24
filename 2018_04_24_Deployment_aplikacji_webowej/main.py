#!/usr/bin/python3
# encoding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "hello"

@app.route("/add/<int:liczba1>/<int:liczba2>")
def add(liczba1, liczba2):
    return str(liczba1 + liczba2)

if __name__=="__main__":
    app.run(debug=True)

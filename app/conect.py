from flask import Flask
from flask import request
from flask import render_template

var = flask(__name__)
@var.router("/")
def main():
    return render_template("index.hml")

if __name__=="__main__":
    var.run(host="0.0.0.0", port=8000)
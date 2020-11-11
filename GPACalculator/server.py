import flask
from flask import render_template, url_for, request
from datetime import datetime
import numpy as np

app = flask.Flask(__name__)


@app.route("/")
def root():
    now = datetime.now()
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))
    return render_template("index.html", t=now.strftime("%m/%d/%Y, %H:%M:%S"))


@app.route("/calculate", methods=["POST"])
def calculate():
    # output = "Thanks for submitting this: " + str(request.args)
    mark = [
        float(request.form["mark1"]),
        float(request.form["mark2"]),
        float(request.form["mark3"]),
    ]
    weight = [
        float(request.form["weightage1"]),
        float(request.form["weightage2"]),
        float(request.form["weightage3"]),
    ]
    sum = 0
    for i in range(len(mark)):
        sum = sum + mark[i] * weight[i]
    return render_template("calc2.html", mark=mark, weight=weight, val=sum)


@app.errorhandler(404)
def invalid_route(e):
    return render_template("404.html")


app.run(debug=True)
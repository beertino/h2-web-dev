import flask
from flask import render_template, url_for, request
from datetime import datetime

app = flask.Flask(__name__)


@app.route("/")
def root():
    now = datetime.now()
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))
    return render_template("index.html", t=now.strftime("%m/%d/%Y, %H:%M:%S"))


@app.route("/calculate")
def calculate():
    # output = "Thanks for submitting this: " + str(request.args)
    mark = [
        float(request.args["mark1"]),
        float(request.args["mark2"]),
        float(request.args["mark3"]),
    ]
    weight = [
        float(request.args["weightage1"]) / 100,
        float(request.args["weightage2"]) / 100,
        float(request.args["weightage3"]) / 100,
    ]
    sum = 0
    for i in range(len(mark)):
        sum = sum + mark[i] * weight[i]
    return "The weighted grade is " + str(sum)


@app.errorhandler(404)
def invalid_route(e):
    return render_template("404.html")


app.run(debug=True)
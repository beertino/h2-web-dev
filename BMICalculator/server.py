import flask
from flask import render_template, url_for, request
from datetime import datetime
from bmi import calculate_bmi

app = flask.Flask(__name__)


@app.route("/")
def root():
    now = datetime.now()
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))
    return render_template("index.html", t=now.strftime("%m/%d/%Y, %H:%M:%S"))


@app.route("/testing")
def welcome():
    return render_template("testing.html")


@app.route("/calcbmi")
def calcbmi():
    mybmi = calculate_bmi(int(request.args["weight"]), int(request.args["height"]))
    name = request.args["name"]
    return render_template("bmi.html", name=name, bmi=mybmi)


@app.errorhandler(404)
def invalid_route(e):
    return render_template("404.html")


app.run(debug=True)
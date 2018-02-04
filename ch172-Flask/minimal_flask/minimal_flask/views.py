from minimal_flask import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


# jinja template with parameters
@app.route("/users/<username>")
def profile(username):
    return render_template("profile.html", username=username, joinDate=None, awards=[])


# handle different HTTP methods
from flask import request
@app.route("/login", methods=["GET", "POST", "DELETE", "PUT"])
def login():
    if request.method == "DELETE" or request.method == "PUT":
        return "This method is not allowed"
    elif request.method == "GET":
        return "This is the login forum"
    elif request.method == "POST":
        return "Username was " + request.form["username"] + " and password was " + request.form["password"]

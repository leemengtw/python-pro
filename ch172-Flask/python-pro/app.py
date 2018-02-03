from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"


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



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
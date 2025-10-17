from flask import Flask, request, session, redirect, request, jsonify, render_template
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods = ["GET", "POST"])
def index():
    if not session.get("enter"):
        return redirect("/landing")
    return render_template("home.html")

@app.route("/landing", methods = ["GET", "POST"])
def landing():
    if request.method == "POST":
        session["enter"] = request.form.get("enter")
    return render_template("landing.html")
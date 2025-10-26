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
    return render_template("home.html", page_id = "home")

@app.route("/landing", methods = ["GET", "POST"])
def landing():
    if request.method == "POST":
        session["enter"] = request.form.get("q")
        return redirect("/")
    return render_template("landing.html", page_id = "landing")

@app.route("/testing")
def testing():
    name = request.args.get("q")

    return jsonify({"msg": f"Hello, {name} nice to meet you"})

if __name__ == "__main__":
    app.run(port=8000, use_reloader=True, debug=True, reloader_type="watchdog")

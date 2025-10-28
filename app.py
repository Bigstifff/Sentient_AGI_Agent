from flask import Flask, request, session, redirect, request, jsonify, render_template
from flask_session import Session
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

api_key = os.getenv("FIREWORKS_API_KEY")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        query = request.json["q"]
        print(query)
        messages = [{
            "role": "user",
            "content": f"Your name is RoboX (don't say your name unless asked, don't tal about your affiliates unless asked, keep responses short under 20 words and simple. You're affiliated with LMT(Like mindes troop), LMT's twitter <a href='https://x.com/LMT_DAO'></a>), you're an ai research partner for DeFi, i.e you analyze yield farms, compare tokens, track protocols in seconds. powered by sentient. Answer comprehensively\nquery: {query}"
        }]

        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

        payload = {"model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
                   "messages": messages,
                   "max_tokens": 120,
                   }
        
        resp = httpx.post("https://api.fireworks.ai/inference/v1/chat/completions", headers=headers, json=payload)
        data = resp.json()
        print(data["choices"][0]["message"]["content"])
        return jsonify({"msg": data["choices"][0]["message"]["content"]})


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

    return jsonify({"msg": f"Hello {name}, nice to meet you"})

if __name__ == "__main__":
    app.run(port=5000, use_reloader=True, debug=True, reloader_type="watchdog")

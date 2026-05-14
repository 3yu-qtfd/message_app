from flask import Flask, render_template, request, redirect
from database import init_db

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        
        init_db()

    return render_template("index.html")

app.run(host="0.0.0.0")

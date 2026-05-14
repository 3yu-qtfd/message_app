from flask import Flask, render_template, request, redirect, url_for
from database import init_db, show_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        #気分をセット
        input_mood = request.form["mood"]

        #気分をDBに受け渡し
        select_message(input_mood)

        return redirect(url_for("index"))

    elif request.method == "GET":

        #init_db()

        returned_message = show_message()

        return render_template(
                "index.html",
                message=returned_message)

app.run(host="0.0.0.0")

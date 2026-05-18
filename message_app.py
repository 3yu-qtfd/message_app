from flask import Flask, render_template, request, redirect, url_for
from database import init_db, select_message

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

    #init_db()

@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":

        #画面で選択した「気分」をセット
        input_mood = request.form["mood"]

        #input_moodをDBに受け渡し、その結果を受け取る
        result = select_message(input_mood)

        #選ばれたメッセージをHTMLに渡す
        return render_template(
                "result.html",
                result=result)

        #return redirect(url_for("index"))

#app.run(host="0.0.0.0")

from flask import Flask, render_template, request, redirect, url_for
from mysql import init_db, write_diary, show_diary

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def result():
    if request.method == "POST":

        #画面で選択した「気分」をinput_moodにセット
        input_mood = request.form["mood"]

        #画面で入力した「日記内容」をinput_contentにセット
        input_content = request.form["content"]

        #input_moodをDBの関数write_diaryに渡す
        write_diary(input_mood, input_content)

#init_db()

    returned_record = show_diary()

    return render_template(
        "index.html",
        records=returned_record)

app.run(host="0.0.0.0")

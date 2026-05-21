from flask import Flask, render_template, request, redirect, url_for
from mysql import init_db, write_diary, show_diary, delete_diary

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def result():
    if request.method == "POST":

        #入力・更新・削除の種類をactionにセット
        action = request.form["action"]

        if action == "insert":
            #画面で選択した「気持ち」をinput_moodにセット
            input_mood = request.form["mood"]

            #画面で入力した「日記内容」をinput_contentにセット
            input_content = request.form["content"]

            #input_moodをDBの関数write_diaryに渡す
            write_diary(input_mood, input_content)

        elif action == "delete":
            #画面で選択したレコードのIDをdelete_idにセット
            delete_id = request.form["delete_id"]

            #delete_idをDBの関数delete_diaryに渡す
            delete_diary(delete_id)

    #テーブル作成
    #init_db()

    #DBの関数show_diaryから受け取った値をreturned_recordにセット
    returned_record = show_diary()

    #index.htmlに、recordsに格納したreturned_recordの値を渡す
    return render_template(
        "index.html",
        records=returned_record)

#アプリ実行
app.run(host="0.0.0.0")

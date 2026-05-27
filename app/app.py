from flask import Flask, render_template, request, redirect, url_for
from mysql import init_db, write_diary, show_diary, delete_diary, update_diary

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/write", methods=["POST"])
def write():
    input_mood = request.form["mood"]
    input_content = request.form["content"]
    write_diary(input_mood, input_content)

    return redirect(url_for("list"))

@app.route("/list", methods=["GET"])
def list():
    returned_record = show_diary()

    #index.htmlに、recordsに格納したreturned_recordの値を渡す
    return render_template(
        "list.html",
        records=returned_record)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    update_content = request.form["update_content"]
    update_diary(update_content, id)

    return redirect(url_for("list"))

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    delete_diary(id)

    return redirect(url_for("list"))

#app.run(host="0.0.0.0")

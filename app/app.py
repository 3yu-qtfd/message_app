from flask import Flask, render_template, request, redirect, url_for
from mysql import init_db, write_diary, show_diary, delete_diary, get_record_by_id, edit_diary
import boto3, json

app = Flask(__name__)

moods = [
    ("happy", "嬉しい"),
    ("relaxed", "リラックス"),
    ("sad", "悲しい"),
    ("anxious", "不安")
]

@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        moods=moods)

@app.route("/write", methods=["POST"])
def write():
    input_mood = request.form["mood"]
    input_content = request.form["content"]
    write_diary(input_mood, input_content)

    client = boto3.client("events")

    response = client.put_events(
        Entries=[
            {
                "EventBusName": "diary_app",
                "Source": "diary.app",
                "DetailType": "diary.created",
                "Detail": json.dumps({
                    "mood": input_mood,
                    "content": input_content
                })
            }
        ]
    )

    print(response)

    return redirect(url_for("list"))

@app.route("/list", methods=["GET"])
def list():
    returned_record = show_diary()

    return render_template(
        "list.html",
        records=returned_record)

@app.route("/edit/<int:edit_id>", methods=["GET", "POST"])
def edit(edit_id):
    if request.method == "POST":
        edit_mood = request.form["edit_mood"]
        edit_content = request.form["edit_content"]

        #print(edit_content)
        
        edit_diary(edit_mood, edit_content, edit_id)
        return redirect(f"/edit/{edit_id}")

    elif request.method == "GET":
        returned_record = get_record_by_id(edit_id)

        #print(returned_record)

        return render_template(
            "edit.html",
            record=returned_record,
            moods=moods)

    #return redirect(url_for("list"))

@app.route("/delete/<int:delete_id>", methods=["POST"])
def delete(delete_id):
    delete_diary(delete_id)

    return redirect(url_for("list"))

app.run(host="0.0.0.0")

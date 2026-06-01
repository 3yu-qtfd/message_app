from flask import Flask, redirect
import pymysql
import os
from dotenv import load_dotenv

#同じディレクトリ内の.envを読み込む
load_dotenv()

#データベース接続処理
def get_connection():
    return pymysql.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DATABASE"),
        cursorclass=pymysql.cursors.DictCursor
    )

#テーブル作成処理（初回のみ実行）
def init_db():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
            CREATE TABLE IF NOT EXISTS diary (
                id INT AUTO_INCREMENT PRIMARY KEY,
                mood VARCHAR(50) NOT NULL,
                content TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                mail_sent BOOLEAN DEFAULT FALSE
                )
                """
            cursor.execute(sql)

            connection.commit()

    finally:
        connection.close()

#INSERT
def write_diary(input_mood, input_content):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
            INSERT INTO `diary` (`mood`, `content`)
            VALUES(%s, %s)
            """
            #デバッグ
            print(f"入力値: {input_mood}")
            print(f"入力値: {input_content}")

            cursor.execute(sql, (input_mood, input_content))

            connection.commit()

    finally:
        connection.close()

#SELECT
def show_diary():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
            SELECT * FROM `diary`
            """
            cursor.execute(sql)

            fetched_record = cursor.fetchall()
            return fetched_record
    
    finally:
        connection.close()

#DELETE
def delete_diary(delete_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
            DELETE FROM `diary`
            WHERE `id` = %s
            """
            cursor.execute(sql, (delete_id,))

            connection.commit()
    
    finally:
        connection.close()

#UPDATE
def update_diary(update_content, update_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE `diary`
            SET `content` = %s
            WHERE `id` = %s
            """
            cursor.execute(sql, (update_content, update_id))

            connection.commit()
    
    finally:
        connection.close()

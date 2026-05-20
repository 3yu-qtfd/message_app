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
            CREATE TABLE IF NOT EXISTS mood_messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                mood VARCHAR(50) NOT NULL,
                output_message TEXT NOT NULL
                )
                """
            cursor.execute(sql)

            connection.commit()

    finally:
        connection.close()

#input_moodの値に応じてメッセージを返す処理
def select_message(input_mood):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
            SELECT output_message
            FROM mood_messages
            WHERE mood = %s
            """
            #デバッグ
            print(f"入力値: {input_mood}")
            
            cursor.execute(sql, (input_mood,))

            result = cursor.fetchone()

            #デバッグ
            print(f"SQL結果: {result}")

            return result

    finally:
        connection.close()

import pymysql

def get_connection():
    return pymysql.connect(
        host='message-app-rds.ct8wi4gaezip.ap-northeast-1.rds.amazonaws.com',
        user='admin',
        password='',
        database='message_app',
        cursorclass=pymysql.cursors.DictCursor
    )

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



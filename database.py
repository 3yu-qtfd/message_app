import sqlite3

DB_NAME = "message_app.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mood_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mood TEXT NOT NULL,
        output_message TEXT NOT NULL
        )
        """)

    conn.commit()
    conn.close()

def show_message(input_mood):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT output_message from mood_messages
    WHERE mood = ?
    """), (input_mood,)

    message = cursor.fetchall()

    cursor.close()
    conn.close

    return message

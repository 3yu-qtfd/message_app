import sqlite3

DB_NAME = "message_app.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
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

def select_message(input_mood):
    print(input_mood)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT output_message FROM mood_messages
    WHERE mood = ?
    """,(input_mood,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

import sqlite3

DB_FILE = "clipboard.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clipboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            type TEXT,
            content TEXT UNIQUE
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("✅ Database initialized")

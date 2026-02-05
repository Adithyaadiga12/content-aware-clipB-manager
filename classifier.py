import pyperclip
import time
import datetime
import re
import sqlite3

DB_FILE = "clipboard.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

# ---------- CLASSIFIER ----------
def classify_text(text: str) -> str:
    text = text.strip()

    if text.startswith("http://") or text.startswith("https://"):
        return "URL"

    if re.match(r"[^@]+@[^@]+\.[^@]+", text):
        return "Email"

    code_patterns = [
        r"\bint\s+\w+",
        r"\bfloat\s+\w+",
        r"\bdouble\s+\w+",
        r"\bclass\s+\w+",
        r"\bdef\s+\w+",
        r"\breturn\b",
        r";\s*$",
        r"\{[^}]*\}",
        r"=\s*[^=]"
    ]

    for pattern in code_patterns:
        if re.search(pattern, text):
            return "Code"

    if len(text.split()) <= 3:
        return "Short Note"

    return "General Text"

print("[RUNNING] Clipboard classifier is active...")

last_text = ""

while True:
    try:
        text = pyperclip.paste().strip()

        if text == "" or text == last_text:
            time.sleep(0.5)
            continue

        last_text = text
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT 1 FROM clipboard WHERE content = ?",
            (text,)
        )

        if cursor.fetchone():
            print("[SKIP] Duplicate")
            conn.close()
            time.sleep(0.5)
            continue

        cursor.execute(
            """
            INSERT INTO clipboard (timestamp, type, content)
            VALUES (?, ?, ?)
            """,
            (
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                classify_text(text),
                text
            )
        )

        conn.commit()
        conn.close()

        print("[SAVED]", text[:50])

    except Exception as e:
        print("[ERROR]", e)

    time.sleep(0.5)

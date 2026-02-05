import pyperclip
import time
import json
import datetime
import os

STORAGE_FILE = "clipboard_storage.json"

# Ensure file exists
if not os.path.exists(STORAGE_FILE):
    with open(STORAGE_FILE, "w") as f:
        json.dump([], f)

def load_storage():
    try:
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    except:
        return []   # if file corrupt

def save_storage(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def classify_clipboard(content: str):
    if content.startswith("http://") or content.startswith("https://"):
        return "URL"
    elif len(content.split()) < 6:
        return "Short Note"
    else:
        return "General Text"

print("[RUNNING] Clipboard classifier is active...")

last_text = ""

while True:
    try:
        text = pyperclip.paste()

        # No change in clipboard
        if text == last_text or text.strip() == "":
            time.sleep(0.5)
            continue

        last_text = text

        items = load_storage()

        # Do not duplicate
        if any(item["content"] == text for item in items):
            print("[SKIP] Duplicate detected:", text)
            time.sleep(0.5)
            continue

        # Build new entry
        new_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": classify_clipboard(text),
            "content": text
        }

        items.append(new_entry)
        save_storage(items)

        print("[SAVED]", new_entry)

    except Exception as e:
        print("[ERROR]", e)

    time.sleep(0.5)

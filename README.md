# 🧠 Context-Aware Clipboard Manager

A simple yet practical desktop project that automatically **classifies and stores clipboard content** (text, code, URLs, etc.) for better organization and future retrieval.
This project focuses on building a **useful system-level utility** using Python with clean modular design.

---

## ✨ Why this project?

While copying content during coding, browsing, or studying, important data often gets lost.
This project aims to solve that by **understanding what you copy** and **organizing it intelligently** instead of treating all clipboard data the same.

---

## 🚀 Features

* 📋 Monitors clipboard activity in real time
* 🧠 Classifies clipboard content (text / code / URLs, etc.)
* 💾 Stores clipboard data in a local SQLite database
* 🔄 Prevents duplicate clipboard entries
* 🧩 Modular code structure for easy extension

---

## 🛠️ Tech Stack

* **Language:** Python
* **Database:** SQLite
* **Libraries:**

  * `sqlite3` – database management
  * `re` – pattern matching for classification
  * Clipboard monitoring libraries (as used in the project)

---

## 📁 Project Structure

```
context-aware-clipboard-manager/
│
├── app.py                     # Main application entry
├── classifier.py              # Clipboard content classification logic
├── clipboard_classifier.py    # Supporting classification rules
├── db.py                      # Database creation & operations
├── output/                    # Generated outputs (if any)
├── .gitignore
└── README.md
```

---

## ▶️ How to Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/Adithyaadiga12/content-aware-clipB-manager.git
   ```

2. **Navigate to the project folder**

   ```bash
   cd content-aware-clipB-manager
   ```

3. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

---

## 🧪 Example Use Case

* Copy a code snippet → stored as **code**
* Copy a website link → stored as **URL**
* Copy normal text → stored as **plain text**

All entries are saved in the database with timestamps for future use.

---

## 📌 What I Learned from This Project

* Working with **system-level utilities**
* Designing **clean modular Python code**
* Using **SQLite for lightweight data storage**
* Applying **basic classification logic** to real-world data
* Using **Git & GitHub** with proper version control

---

## 🔮 Future Improvements

* GUI interface for browsing clipboard history
* Search & filter functionality
* Cloud sync support
* Better ML-based classification

---

## 🙋‍♂️ About Me

I’m a student passionate about **software development and problem-solving**, building practical projects to strengthen my fundamentals and real-world skills.

Feel free to explore the repository or suggest improvements!

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it really helps and motivates me 🙂

---

## ✅ Next steps (do this now)

1. Create the file:

   ```bat
   notepad README.md
   ```
2. Paste the content above
3. Save it
4. Commit & push:

   ```bat
   git add README.md
   git commit -m "Added project README"
   git push
   ```

---


import streamlit as st
import sqlite3

DB_FILE = "clipboard.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

st.set_page_config(page_title="Clipboard Manager", layout="wide")
st.title("📋 Context-Aware Clipboard Manager (SQLite)")

# ---------- FILTERS ----------
col1, col2 = st.columns(2)

with col1:
    selected_category = st.selectbox(
        "📂 Filter by category",
        ["All", "URL", "Code", "Email", "Short Note", "General Text"]
    )

with col2:
    search_query = st.text_input("🔍 Search")

# ---------- REMOVE DUPLICATES ----------
if st.button("🧹 Remove Duplicates"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM clipboard
        WHERE id NOT IN (
            SELECT MIN(id) FROM clipboard GROUP BY content
        )
    """)
    conn.commit()
    conn.close()
    st.success("Duplicates removed!")

st.divider()

# ---------- LOAD DATA ----------
conn = get_connection()
cursor = conn.cursor()

query = "SELECT timestamp, type, content FROM clipboard"
params = []

if selected_category != "All":
    query += " WHERE type = ?"
    params.append(selected_category)

if search_query:
    query += " AND" if "WHERE" in query else " WHERE"
    query += " (content LIKE ? OR type LIKE ?)"
    params.extend([f"%{search_query}%", f"%{search_query}%"])

query += " ORDER BY timestamp DESC"

cursor.execute(query, params)
rows = cursor.fetchall()
conn.close()

# ---------- DISPLAY ----------
if not rows:
    st.info("No clipboard items found.")
else:
    st.subheader(f"📌 Clipboard History ({len(rows)} items)")

    for ts, typ, content in rows:
        st.markdown(
            f"""
            <div style="padding:12px;margin-bottom:10px;
                        border:1px solid #ccc;border-radius:8px;">
                <b>🕒 {ts}</b><br>
                <b>Type:</b> <span style="color:#2e7d32;">
                {typ}</span><br><br>
                <pre style="white-space:pre-wrap;">{content}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )

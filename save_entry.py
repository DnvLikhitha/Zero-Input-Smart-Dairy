import sqlite3
from datetime import datetime

def save_to_db(entry):
    conn = sqlite3.connect("diary.db")
    cursor = conn.cursor()
    today = datetime.now().date().isoformat()
    # Remove any existing entry for today
    cursor.execute("DELETE FROM diary WHERE entry_date = ?", (today,))
    # Insert the new entry
    cursor.execute("INSERT INTO diary (entry_date, content) VALUES (?, ?)", (today, entry))
    conn.commit()
    conn.close()
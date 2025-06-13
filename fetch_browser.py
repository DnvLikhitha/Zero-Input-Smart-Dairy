import sqlite3
import os

def get_browser_history():
    history_path = os.path.expanduser("~/.config/google-chrome/Default/History")
    if not os.path.exists(history_path):
        return "No browser history found."

    try:
        conn = sqlite3.connect(history_path)
        cursor = conn.cursor()
        cursor.execute("SELECT url, title FROM urls ORDER BY last_visit_time DESC LIMIT 5")
        rows = cursor.fetchall()
        conn.close()

        return "\n".join([f"{title} - {url}" for url, title in rows])
    except Exception as e:
        return f"Could not read history: {e}"

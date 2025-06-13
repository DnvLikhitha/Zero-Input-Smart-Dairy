![Zero-Input-Smart-Diary](https://socialify.git.ci/DnvLikhitha/Zero-Input-Smart-Diary/image?font=Inter&language=1&name=1&theme=Dark)
# 📘 Zero Input Smart Diary: Your Day, Reflected

**Zero Input Smart Dairy** is a smart, personal journaling assistant that automatically reflects on your day. It pulls in your Gmail emails, Google Calendar events, and Chrome history, then uses **Google Gemini AI** to generate a warm, reflective diary entry. Your diary entry is securely stored in a local SQLite database.

---

## 🧠 Features

- 📧 Fetches latest Gmail messages
- 📅 Collects today's Google Calendar events
- 🌐 Reads recent Chrome browsing history
- ✍️ Uses Gemini AI for writing beautiful diary entries
- 🗃 Stores one entry per day in a local SQLite DB

---

## 📂 Project Structure

```
├── app.py               # Streamlit Web Interface
├── diary.py             # Main script to run the diary
├── fetch_email.py       # Fetches recent Gmail messages
├── fetch_calendar.py    # Fetches today's Google Calendar events
├── fetch_browser.py     # Retrieves recent Chrome browsing history
├── mood_input.py        # Formats mood input
├── generate_entry.py    # Uses Gemini API to generate diary entry
├── save_entry.py        # Saves entry to SQLite DB
├── credentials.json     # OAuth2 credentials (you provide)
├── diary.db             # SQLite DB (auto-generated)
└── requirements.txt     # Python dependencies
```

---

## 🚀 Getting Started

1. **Clone the repo**

   ```sh
   git clone https://github.com/DnvLikhitha/Zero-Input-Smart-Dairy.git
   cd Zero-Input-Smart-Dairy
   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up Google API access**
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create a project → Enable Gmail and Calendar APIs
   - Create OAuth 2.0 Desktop credentials → Download `credentials.json` and place it in the project root

4. **Get your Gemini API Key**
   - Go to [Google MakerSuite](https://makersuite.google.com/app/apikey)
   - Paste your key into `generate_entry.py` as instructed in the code

5. **Run the diary**

   ```sh
   streamlit run app.py
   ```

   Or in Python:

   ```python
   from diary import run_diary
   run_diary("Joyful")
   ```

---

## 🗂 How It Works

| Step           | Module              | Description                           |
| -------------- | ------------------- | ------------------------------------- |
| Fetch Gmail    | `fetch_email.py`    | Retrieves your 5 latest email snippets|
| Fetch Calendar | `fetch_calendar.py` | Gets today’s Google Calendar events   |
| Get History    | `fetch_browser.py`  | Reads 5 most recent Chrome URLs       |
| Format Mood    | `mood_input.py`     | Wraps mood input in a sentence        |
| Generate Entry | `generate_entry.py` | Uses Gemini API to write a diary entry|
| Save Entry     | `save_entry.py`     | Saves diary entry to SQLite           |

---

## 💾 Database Schema

**Table:** `diary`

| Column      | Type | Description                  |
| ----------- | ---- | ----------------------------|
| entry_date  | TEXT | YYYY-MM-DD (Primary Key)     |
| content     | TEXT | The diary entry              |

---

## 🔒 Privacy

- All data is local — no cloud storage
- Only read-only Google access requested
- Gemini API key is used securely (you provide it)

---

## 💡 Future Improvements

- Mood visualization dashboard
- Sentiment analysis over time
- Web/mobile interface
- End-to-end encryption

---

## 🙋 Contribution

Pull requests and feature ideas are welcome! Please fork and contribute ❤️

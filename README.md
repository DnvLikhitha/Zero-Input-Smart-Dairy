# Zero-Input-Smart-Dairy
This project is an intelligent personal diary generator that automatically creates a warm, reflective daily diary entry using your:

- Recent Gmail messages  
- Google Calendar events  
- Chrome browser history  
- Your mood (user input)

All entries are generated with Google's Gemini AI and stored locally in an SQLite database.

---

## Features

- Reads your last 5 Gmail snippets
- Fetches today’s calendar events
- Gets your last 5 visited browser URLs
- Uses Gemini AI (`gemini-2.0-flash`) to write a diary entry
- Saves entries to a SQLite database (`diary.db`)
- Local execution and secure Google OAuth 2.0 authentication

---

## Getting Started

### Prerequisites

- Python 3.8+
- Google Cloud project with Gmail & Calendar APIs enabled
- Google Chrome (if using browser history)
- A Gemini AI API key

### 📁 Folder Structure
.
├── diary.py
├── fetch_gmail.py
├── fetch_calendar.py
├── fetch_browser.py
├── mood_input.py
├── generate_entry.py
├── save_entry.py
├── credentials.json
└── README.md




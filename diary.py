from datetime import datetime
from fetch_gmail import get_recent_emails
from fetch_calendar import get_todays_events
from fetch_browser import get_browser_history
from mood_input import get_mood
from generate_entry import generate_diary_entry
from save_entry import save_to_db

def run_diary(mood):
    emails = get_recent_emails()
    calendar = get_todays_events()
    browser = get_browser_history()
    mood_str = get_mood(mood)
    today_str = datetime.now().strftime("%B %d, %Y")

    entry = generate_diary_entry(emails, calendar, browser, mood_str, today_str)
    print("\nGenerated Diary Entry:\n")
    print(entry)

    save_to_db(entry)
    return entry
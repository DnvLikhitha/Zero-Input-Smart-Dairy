import google.generativeai as genai

genai.configure(api_key="your_api_key")

def generate_diary_entry(emails, calendar, browser, mood, date):
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
Write a daily diary entry for {date} based on:
Emails: {emails}
Calendar: {calendar}
Browser: {browser}
Mood: {mood}
Make it personal, warm, and reflective.
"""

    response = model.generate_content(prompt)
    return response.text
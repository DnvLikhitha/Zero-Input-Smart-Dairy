import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import subprocess
from export_pdf import export_to_pdf
import plotly.express as px
from diary import run_diary

DB_PATH = "diary.db"

def get_entries():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT entry_date, content FROM diary ORDER BY entry_date DESC")
    data = cursor.fetchall()
    conn.close()
    return pd.DataFrame(data, columns=["Date", "Entry"])

def get_today_entry():
    today = datetime.now().date().isoformat()
    df = get_entries()
    return df[df["Date"] == today]

st.set_page_config(page_title="Smart Diary", layout="centered")
st.title("📓 Zero-Input Smart Diary")

menu = st.sidebar.selectbox("Menu", ["📅 Today", "📖 Past Entries"])

if menu == "📅 Today":
    st.header("Today's Diary")

    # Mood input section
    mood = st.radio("How are you feeling today? (😊😐😔😠)", ["😊", "😐", "😔", "😠"], horizontal=True)

    # Generate button
    if st.button("🪄 Generate Today's Entry"):
        entry = run_diary(mood)  # Pass mood from UI
        """ st.write(entry) """

    today_data = get_today_entry()

    if not today_data.empty:
        st.subheader("Generated Diary Entry:")
        st.markdown(f"**{today_data['Date'].values[0]}**")
        st.text_area("Diary Entry", today_data["Entry"].values[0], height=400, label_visibility="collapsed")
        #st.markdown(f"**Mood**: {today_data['Mood'].values[0]}")

        if st.download_button("Download as PDF", export_to_pdf(today_data["Entry"].values[0]), file_name="today_diary.pdf"):
            st.success("Downloaded!")
    else:
        st.warning("No diary entry found for today. Click 'Generate' above first.")

elif menu == "📖 Past Entries":
    df = get_entries()
    selected_date = st.date_input("Select date to view entry")
    date_str = selected_date.isoformat()
    entry = df[df["Date"] == date_str]

    if not entry.empty:
        st.text_area("Entry", entry["Entry"].values[0], height=300)
        #st.markdown(f"**Mood**: {entry['Mood'].values[0]}")
        if st.download_button("Download as TXT", entry["Entry"].values[0].encode(), file_name=f"{date_str}.txt"):
            st.success("TXT Downloaded")
    else:
        st.info("No entry found for this date.")

#elif menu == "📈 Mood Chart":
#    df = get_entries()
#    if df.empty:
#        st.warning("No mood data yet.")
#    else:
#        mood_map = {"😊": 2, "😐": 1, "😔": 0, "😠": -1}
#        df["Mood Score"] = df["Mood"].map(mood_map)
#        fig = px.line(df, x="Date", y="Mood Score", title="Mood Trend Over Time", markers=True)
#        st.plotly_chart(fig)

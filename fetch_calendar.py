from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime

def get_todays_events():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', scopes=['https://www.googleapis.com/auth/calendar.readonly'])
    creds = flow.run_local_server(port=0)
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    end = (datetime.datetime.utcnow() + datetime.timedelta(hours=24)).isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=end).execute()
    events = events_result.get('items', [])

    return "\n".join([f"{event['summary']} at {event.get('start', {}).get('dateTime', 'Unknown time')}" for event in events])

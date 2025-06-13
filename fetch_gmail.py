from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def get_recent_emails():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', scopes=['https://www.googleapis.com/auth/gmail.readonly'])
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_data.get('snippet', '')
        emails.append(snippet)
    return "\n".join(emails)

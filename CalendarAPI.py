from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datefinder

# Authentication to use the CalendarAPI
flow = InstalledAppFlow.from_client_secrets_file('clientsecret.json', scopes=['https://www.googleapis.com/auth/calendar'])
flow.run_local_server()
credentials = flow.credentials
service = build("calendar", "v3", credentials=credentials)

# Create a Google Calendar event with the specified arguments.
def create_event(start_time_str, end_time_str, summary, description=None, location=None):
    start_matches = list(datefinder.find_dates(start_time_str))
    end_matches = list(datefinder.find_dates(end_time_str))
    if len(start_matches):
        start_time = start_matches[0]
    if len(end_matches):
        end_time = end_matches[0]

    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'America/Los_Angeles',
        },
    }
    return service.events().insert(calendarId='primary', body=event).execute()




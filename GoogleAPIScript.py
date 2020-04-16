import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datefinder

# Authorize the correct google account using the .json file from
scopes = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive", 'https://www.googleapis.com/auth/calendar']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scopes)

# Read/Parse information in the Google Sheet
client = gspread.authorize(creds)
sheet = client.open('shifts-by-client').sheet1
data = sheet.get_all_records()

flow = InstalledAppFlow.from_client_secrets_file('clientsecret.json', scopes=['https://www.googleapis.com/auth/calendar'])
flow.run_local_server()
credentials = flow.credentials
service = build("calendar", "v3", credentials=credentials)

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

# Define variables and iterate through each item. Then create calendar events on Google Calendar.
# Data is a list of dictionaries with each dictionary containing shift info. This iterates through each dictionary and creates a calendar event.
for dict in data:
    client_name = dict['Client']
    city = dict['Client City']
    postal_code = dict['Client Postal Code']
    # str(postal_code)
    # location = city + ' ' + postal_code
    start_time = dict['Next Occurrence Start']
    end_time = dict['Next Occurrence End']
    create_event(start_time, end_time, 'This is an open shift', '123test', city)

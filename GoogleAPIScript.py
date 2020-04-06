import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from CalendarAPI import create_event
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datefinder

# Authorize the correct google account using the .json file from
scopes = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive", 'https://www.googleapis.com/auth/calendar']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scopes)

# Read/Parse information in the Google Sheet
client = gspread.authorize(creds)
sheet = client.open('shifts-by-client').sheet1
service = build("calendar", "v3", credentials=creds)

data = sheet.get_all_records()

flow = InstalledAppFlow.from_client_secrets_file('clientsecret.json', scopes=['https://www.googleapis.com/auth/calendar'])
flow.run_local_server()
credentials = flow.credentials
service = build("calendar", "v3", credentials=credentials)

# Define variables and iterate through each item. Then create calendar events on Google Calendar.
# Data is a list of dictionaries with each dictionary containing shift info. This iterates through each dictionary and creates a calendar event.
# create_event function is being pulled from a separate file.
for dict in data:
    client_name = dict['Client']
    city = dict['Client City']
    postal_code = dict['Client Postal Code']
    # str(postal_code)
    # location = city + ' ' + postal_code
    start_time = dict['Next Occurrence Start']
    end_time = dict['Next Occurrence End']
    create_event(start_time, end_time, 'This is an open shift', '123test', city)

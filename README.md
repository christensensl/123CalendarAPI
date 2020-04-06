# 123CalendarAPI

#This was a side project I did in my spare time to give our team of caregivers the ability to see open shifts in their region. 
It uses a .xlsx export from our company CRM that contains all of the shift information for a given time period. 
That spreadsheet is uploaded to Google Sheets and the data is used to create calendar events using the Google Calendar API.
The ultimate goal is to have a calendar that is viewable by caregivers so that staffing shifts is more efficient for managers.

Extra Notes:
-gspread was used to parse the spreadsheet data as it was simpler to get started than the Google Sheets API. 
-The Google Calendar API currently requires authorization each time it is run.
-This code also uses a client_secret.json file which I have left out because it contains specific information for the google account.

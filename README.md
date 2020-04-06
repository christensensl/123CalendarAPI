# 123CalendarAPI

#The was a side project I did in my spare time to give our team of caregivers the ability to see open shifts in their region. 
It uses a .xlsx export from our company CRM that contains all of the shift information. 
That spreadsheet is uploaded to Google Sheets and the data is used to create calendar events using the Google Calendar API.
The goal was to have a calendar that was shareable and viewable by caregivers so that staffing shifts would be more efficient.

Extra Notes:
-gspread was used to parse the spreadsheet data as it was simpler to get started than the Google Sheets API. 
-The Google Calendar API works but requires authorization each time it is run.

# python-student-picker
A terminal-based application for "randomly" selecting a student.  Other features like pop-quiz mode and basket mode, which will choose students one at a time until all have been selected, then they all go back in.

# Todo Items
- Need to write status changes to sheet
- Need to push item models into list models (rename SimpleItemModel and BasketItemModel to be list models)
- Validate that things work ok even with disconnected sheets

# Help
- Delete token.json if your token expires

# Initial Setup
- Need to get credentials.json (containing client id and client secret) from google apis following the documentation here: https://developers.google.com/sheets/api/quickstart/python
and here: https://console.cloud.google.com/apis/credentials

Essentially the credentials.json gets downloaded from the google api page where you can see the client id and client secret.

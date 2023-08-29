# python-student-picker
A terminal-based application for "randomly" selecting a student.  Other features like pop-quiz mode and basket mode, which will choose students one at a time until all have been selected, then they all go back in.

# Todo Items
- Need to write status changes to sheet
- Need to push item models into list models (rename SimpleItemModel and BasketItemModel to be list models)
- Validate that things work ok even with disconnected sheets

# Help
- Delete token.json if your token expires

# Initial Setup
## credentials.json
- Need to get credentials.json (containing client id and client secret) from google apis following the documentation here: https://developers.google.com/sheets/api/quickstart/python
and here: https://console.cloud.google.com/apis/credentials

Essentially the credentials.json gets downloaded from the google api page where you can see the client id and client secret.

## sheet id
You can extract the sheet id from the url when the sheet is open in the browser.
So for a url like: https://docs.google.com/spreadsheets/d/1u2gtJuBBkpAbXXXXXafyhCKn2hf-p8-D7DWfjlwZ0sU/edit#gid=0
The sheet id would be: 1u2gtJuBBkpAbXXXXXafyhCKn2hf-p8-D7DWfjlwZ0sU
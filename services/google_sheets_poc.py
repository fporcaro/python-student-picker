import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

GOOGLE_SHEET_SCOPES_ENV_KEY = "GOOGLE_SHEET_SCOPES"
GOOGLE_SHEET_SPREADSHEET_ID_ENV_KEY = "GOOGLE_SHEET_SPREADSHEET_ID"
GOOGLE_SHEET_HEADER_RANGE_NAME_ENV_KEY = "GOOGLE_SHEET_HEADER_RANGE_NAME"
GOOGLE_SHEET_ITEMS_RANGE_NAME_ENV_KEY = "GOOGLE_SHEET_ITEMS_RANGE_NAME"
GOOGLE_SHEET_HISTORY_RANGE_NAME_ENV_KEY = "GOOGLE_SHEET_HISTORY_RANGE_NAME"


def print_data():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # If modifying these scopes, delete the file token.json.
    scopes_str = os.environ[GOOGLE_SHEET_SCOPES_ENV_KEY]
    scopes = scopes_str.split(",")

    # The ID and range of a sample spreadsheet.
    spreadsheet_id = os.environ[GOOGLE_SHEET_SPREADSHEET_ID_ENV_KEY]
    sheet_range_name = os.environ[GOOGLE_SHEET_ITEMS_RANGE_NAME_ENV_KEY]

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=sheet_range_name).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(f"{row[0]}, {row[1], row[2] ,row[3]}")
    except HttpError as err:
        print(err)
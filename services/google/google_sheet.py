import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import logging

from typing import List

INPUT_VALUE_OPTION_RAW = "RAW"
INPUT_VALUE_OPTION_USER_ENTERED = "USER_ENTERED"


class GoogleSheet:
    def __init__(self, sheet_id, scopes, credentials_filename, token_filename):
        self.sheet_id = sheet_id
        self.scopes = scopes
        self.credentials_filename = credentials_filename
        self.token_filename = token_filename
        self.creds = None
        self.sheet_service = None

    def get_stored_credentials(self):
        creds = None
        if os.path.exists(self.token_filename):
            creds = Credentials.from_authorized_user_file(self.token_filename, self.scopes)
        return creds

    def get_and_save_credentials(self):
        # The token file (token_filename, usually token.json) stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        creds = self.get_stored_credentials()
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_filename, self.scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_filename, 'w') as token_file:
                token_file.write(creds.to_json())
        self.creds = creds
        return creds

    def connect_service(self):
        if self.creds is None:
            self.get_and_save_credentials()
        try:
            service = build('sheets', 'v4', credentials=self.creds)

            # Call the Sheets API
            self.sheet_service = service.spreadsheets()
        except HttpError as err:
            logging.error(f"Error {err} trying to connect to Google Sheets)")

    # Read Support
    def read_range(self, range_name):
        result = self.sheet_service.values().get(spreadsheetId=self.sheet_id,
                                                 range=range_name).execute()
        values = result.get('values', [])
        return values

    def extract_single_value(self, result):
        return result[0][0]

    def extract_objects(self, result, column_headers):
        objects = []
        for row in result:
            object = {}
            column_index = 0
            for column_name in column_headers:
                if column_index < len(row):
                    object[column_name] = row[column_index]
                column_index += 1
            objects.append(object)
        return objects

    def read_single_cell(self, cell_address):
        return self.extract_single_value(self.read_range(cell_address))

    def read_objects_from_range(self, range_name, column_headers):
        result = self.read_range(range_name=range_name)
        return self.extract_objects(result=result, column_headers=column_headers)

    # Write Support
    def create_range_values_from_single_cell(self, cell_value):
        return [[cell_value]]

    def write_single_cell(self, cell_address, cell_value):
        return self.update_range(range_name=cell_address, values=self.create_range_values_from_single_cell(cell_value=cell_value))

    def create_range_values_from_objects(self, objects, column_headers):
        rows = []
        for object in objects:
            row = []
            for column_name in column_headers:
                row.append(object.get(column_name))
            rows.append(row)
        return rows

    def update_range(self, range_name, values: List[list], input_value_option=INPUT_VALUE_OPTION_USER_ENTERED):
            try:
                data = [
                    {
                        'range': range_name,
                        'values': values
                    },
                    # Additional ranges to update ...
                ]
                body = {
                    'valueInputOption': input_value_option,
                    'data': data
                }
                result = self.sheet_service.values().batchUpdate(
                    spreadsheetId=self.sheet_id, body=body).execute()
                logging.info(f"{(result.get('totalUpdatedCells'))} cells updated.")
                return result
            except HttpError as error:
                logging.error(f"An error occurred: {error}")
                return error


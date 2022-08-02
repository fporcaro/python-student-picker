from services.google.google_sheet import GoogleSheet

READ_WRITE_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SHEET_ITEM_MASTER = "Item Master"
SHEET_SELECTION_HISTORY = "Selection History"
RANGE_MODE = f"{SHEET_ITEM_MASTER}!A3"
RANGE_MODEL = f"{SHEET_ITEM_MASTER}!B3"
RANGE_POP_QUIZ_ITEM = f"{SHEET_ITEM_MASTER}!A6:D6"
RANGE_STUDENT_ITEMS = f"{SHEET_ITEM_MASTER}!A7:D"
RANGE_SELECTION_HISTORY = f"{SHEET_SELECTION_HISTORY}!A5:D"

ITEM_COLUMN_NUMBER = 'number'
ITEM_COLUMN_NAME = 'name'
ITEM_COLUMN_PREVIOUSLY_SELECTED = 'previously_selected'
ITEM_COLUMN_ENABLED = 'enabled'
ITEM_COLUMN_HEADERS = [ITEM_COLUMN_NUMBER, ITEM_COLUMN_NAME, ITEM_COLUMN_PREVIOUSLY_SELECTED, ITEM_COLUMN_ENABLED]
SELECTION_HISTORY_COLUMN_HEADERS = ['date_time', 'model', 'current_items_after', 'previous_selections_after']


class StudentPickerSheet:
    def __init__(self, sheet_id):
        self.sheet = GoogleSheet(sheet_id=sheet_id, scopes=READ_WRITE_SCOPES, credentials_filename='credentials.json',
                                 token_filename='token.json')
        self.sheet.get_and_save_credentials()
        self.sheet.connect_service()

    def read_mode(self):
        return self.sheet.read_single_cell(RANGE_MODE)

    def read_model(self):
        return self.sheet.read_single_cell(RANGE_MODEL)

    def read_pop_quiz_item(self):
        # A range returns multiple rows/objects
        range_result = self.sheet.read_objects_from_range(RANGE_POP_QUIZ_ITEM, column_headers=ITEM_COLUMN_HEADERS)
        return range_result[0]

    def read_student_items(self):
        return self.sheet.read_objects_from_range(RANGE_STUDENT_ITEMS, column_headers=ITEM_COLUMN_HEADERS)

    def write_mode(self, mode):
        return self.sheet.write_single_cell(RANGE_MODE, mode)

    def write_model(self, model_name):
        return self.sheet.write_single_cell(RANGE_MODEL, model_name)


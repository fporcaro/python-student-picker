import logging

from src.persistence.item_factory import ItemFactory, ITEM_COLUMN_HEADERS
from src.services.google.google_sheet import GoogleSheet

READ_WRITE_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SHEET_ITEM_MASTER = "Item Master"
SHEET_SELECTION_HISTORY = "Selection History"
RANGE_MODE = f"{SHEET_ITEM_MASTER}!A3"
RANGE_MODEL = f"{SHEET_ITEM_MASTER}!B3"
RANGE_POP_QUIZ_ITEM = f"{SHEET_ITEM_MASTER}!A6:E6"
RANGE_STUDENT_ITEMS = f"{SHEET_ITEM_MASTER}!A7:E"
RANGE_SELECTION_HISTORY = f"{SHEET_SELECTION_HISTORY}!A5:D"

SELECTION_HISTORY_COLUMN_HEADERS = ['date_time', 'model', 'current_items_after', 'previous_selections_after']


class StudentPickerSheet:
    def __init__(self, sheet_id):
        self.sheet = GoogleSheet(sheet_id=sheet_id, scopes=READ_WRITE_SCOPES, credentials_filename='./credentials.json',
                                 token_filename='./token.json')
        self.sheet.get_and_save_credentials()
        self.sheet.connect_service()

    def read_mode(self):
        return self.sheet.read_single_cell(RANGE_MODE)

    def read_model(self):
        return self.sheet.read_single_cell(RANGE_MODEL)

    def read_pop_quiz_item(self):
        item_dicts = self.sheet.read_objects_from_range(RANGE_POP_QUIZ_ITEM, column_headers=ITEM_COLUMN_HEADERS)
        if len(item_dicts) > 1:
            logging.error(f"Read more than one pop quiz Item: {item_dicts} from range: {RANGE_POP_QUIZ_ITEM}")
            return None
        return self.convert_to_item_model(item_dict=item_dicts[0])

    def read_student_items(self):
        item_dicts = self.sheet.read_objects_from_range(RANGE_STUDENT_ITEMS, column_headers=ITEM_COLUMN_HEADERS)
        return self.convert_to_item_models(item_dicts=item_dicts)

    def convert_to_item_models(self, item_dicts):
        items = []
        for item_dict in item_dicts:
            items.append(self.convert_to_item_model(item_dict))
        return items

    def convert_to_item_model(self, item_dict):
        return ItemFactory.create_item_model(item_dict)

    def write_mode(self, mode):
        return self.sheet.write_single_cell(RANGE_MODE, mode)

    def write_model(self, model_name):
        return self.sheet.write_single_cell(RANGE_MODEL, model_name)

    def write_student_items(self, student_items):
        student_items.sort()
        item_dicts = []
        for item in student_items:
            item_dicts.append(ItemFactory.create_dict_from_item_model(item_model=item))
        return self.sheet.write_range(RANGE_STUDENT_ITEMS, item_dicts, column_headers=ITEM_COLUMN_HEADERS)

    def write_pop_quiz_item(self, pop_quiz_item, pop_quiz_item_enabled, pop_quiz_item_previously_selected):
        item_dicts = []
        item_dicts.append(ItemFactory.create_dict_from_item_model(item_model=pop_quiz_item))
        return self.sheet.write_range(RANGE_POP_QUIZ_ITEM, item_dicts, column_headers=ITEM_COLUMN_HEADERS)

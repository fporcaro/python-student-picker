import os

from src.model.basket_item_model import BasketItemModel
from src.view.item_reveal_view import ItemRevealView
from src.model.simple_item_model import SimpleItemModel
from src.persistence.student_item_model_google_sheet_broker import StudentPickerManagerGoogleSheetBroker
from src.model.student_picker_manager import StudentPickerManager
from src.persistence.student_picker_sheet import StudentPickerSheet
from dotenv import load_dotenv

load_dotenv(".env")
lines = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']


def run_reveal():
    item_reveal_view = ItemRevealView(default_initial_duration=1.0)
    item_reveal_view.reveal_value_dramatic("Person One", ["Person Two", "Person Three", "Person Four"])


def run_student_picker():
    items_str = os.environ["TEST_ITEMS"]
    items = items_str.split(", ")
    pop_quiz_item = "Pop Quiz"
    list_item_model = SimpleItemModel(main_items=items, pop_quiz_item=pop_quiz_item)
    basket_item_model = BasketItemModel(main_items=items, pop_quiz_item=pop_quiz_item)
    student_picker = StudentPickerManager(list_model=list_item_model, basket_model=basket_item_model)
    student_picker.start()
    student_picker.process_input_loop()


def use_student_picker_sheet():
    sheet_id = os.environ["GOOGLE_SHEET_SPREADSHEET_ID"]
    student_picker_sheet = StudentPickerSheet(sheet_id=sheet_id)
    broker = StudentPickerManagerGoogleSheetBroker(student_picker_sheet=student_picker_sheet)
    student_picker_manager = broker.create_manager_from_sheet()
    student_picker_manager.start()
    student_picker_manager.process_input_loop()


print('main.py module name is %s' % __name__)
if __name__ == '__main__':
    use_student_picker_sheet()


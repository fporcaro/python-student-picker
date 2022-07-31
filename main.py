import os
from time import sleep

from basket_item_model import BasketItemModel
from item_reveal_view import ItemRevealView
from simple_item_model import SimpleItemModel
from student_picker_manager import StudentPickerManager
from wheel_view_model import WheelViewModel
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
    student_picker = StudentPickerManager(list_model=list_item_model, basket_model=basket_item_model, pop_quiz_item=pop_quiz_item)
    student_picker.start()
    student_picker.process_input_loop()


if __name__ == '__main__':
    run_student_picker()


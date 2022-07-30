import msvcrt
from time import sleep

from basket_item_model import BasketItemModel
from item_reveal_view import ItemRevealView
from simple_item_model import SimpleItemModel
from student_picker_manager import StudentPickerManager
from terminal_wheel_view import TerminalWheelView
from wheel_view_model import WheelViewModel


lines = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']


def run_display_wheel():
    wheel_view_model = WheelViewModel(line_items=lines)
    terminal_wheel_view = TerminalWheelView(wheel_view_model=wheel_view_model, starting_index=6)
    count = 100
    for item_index in range(count):
        terminal_wheel_view.print_wheel()
        wheel_view_model.increment_wheel()
        sleep(0.01)


def run_reveal():
    item_reveal_view = ItemRevealView(default_initial_duration=1.0)
    item_reveal_view.reveal_value_dramatic("Frank Porcaro", ["Larry Johns", "Rob Russell", "Kristina Contino"])


def run_randomizer():
    items = ["Frank Porcaro", "Sam Porcaro", "Ericka Miranda", "Rob Russell", "Matt Short", "Kristina Contino"]
    pop_quiz_item = "Pop Quiz"
    list_item_model = SimpleItemModel(main_items=items, pop_quiz_item=pop_quiz_item)
    basket_item_model = BasketItemModel(main_items=items, pop_quiz_item=pop_quiz_item)
    randomizer = StudentPickerManager(list_model=list_item_model, basket_model=basket_item_model, pop_quiz_item=pop_quiz_item)
    randomizer.start()
    randomizer.process_input_loop()


if __name__ == '__main__':
    run_randomizer()


import msvcrt
from time import sleep

from item_reveal_view import ItemRevealView
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
    item_reveal_view = ItemRevealView(default_initial_duration=1.5)
    item_reveal_view.reveal_value("Frank Porcaro")


def run_get_input():
    input_char = msvcrt.getche()


if __name__ == '__main__':
    run_get_input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

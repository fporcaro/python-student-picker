import terminal
from time import sleep

from terminal_wheel_view import TerminalWheelView
from wheel_view_model import WheelViewModel


lines = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']


def run():
    wheel_view_model = WheelViewModel(line_items=lines)
    terminal_wheel_view = TerminalWheelView(wheel_view_model=wheel_view_model, starting_index=6)
    count = 100
    for item_index in range(count):
        terminal_wheel_view.print_wheel()
        wheel_view_model.increment_wheel()
        sleep(0.05)


if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import terminal
from time import sleep
from wheel import print_wheel, get_next_index


def run():
    lines = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
    next_first_line = 0
    for count in range(10):
        print_wheel(line_items=lines, starting_index=count, lines_to_display=5)
        next_first_line = get_next_index(line_items=lines, current_index=next_first_line)
        print('')
        sleep(3)


if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from sys import stdout
from time import sleep

ESC_PREFIX = f'\033['


def esc(code, params=[]):
    param_str = ''
    for param in params:
        if param_str == '':
            param_prefix = ''
        else:
            param_prefix = ';'
        param_str += f'{param_prefix}{param}'
    return f'{ESC_PREFIX}{param_str}{code}'


def save_cursor_pos():
    write(esc('s'))


def restore_cursor_pos():
    write(esc('u'))


def set_cursor_position(row, col):
    write(esc('H', [row, col]))


def cursor_previous_line(lines=1):
    write(esc('F', [lines]))


def cursor_next_line(lines=1):
    write(esc('E', [lines]))


def erase_to_end_of_line():
    write(esc('K'))


def erase_to_start_of_line():
    write(esc('K', [1]))


def erase_entire_line():
    write(esc('K', [2]))


def erase_in_display(function=0):
    write(esc('J', [function]))


def cursor_position_absolute(pos):
    write(esc('G', [pos]))


def write(text="\n"):
    stdout.write(text)
    stdout.flush()


def writew(text="\n", wait=0.5):
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(wait)


class fg:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"

    @classmethod
    def rgb(cls, r: int, g: int, b: int): return f"\u001b[38;2;{r};{g};{b}m"


class bg:
    black = "\u001b[40m"
    red = "\u001b[41m"
    green = "\u001b[42m"
    yellow = "\u001b[43m"
    blue = "\u001b[44m"
    magenta = "\u001b[45m"
    cyan = "\u001b[46m"
    white = "\u001b[47m"

    @classmethod
    def rgb(cls, r: int, g: int, b: int): return f"\u001b[48;2;{r};{g};{b}m"


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
    return esc('s')


def restore_cursor_pos():
    return esc('u')


def set_cursor_position(row, col):
    return esc('H', [row, col])


def cursor_previous_line(lines):
    return esc('F', [lines])


def cursor_next_line(lines):
    return esc('E', [lines])


def erase_to_end_of_line():
    return esc('K')


def erase_to_start_of_line():
    return esc('K', [1])

def erase_entire_line():
    return esc('K', [2])
def erase_in_display(function=0):
    return esc('J', [function])


def cursor_position_absolute(pos):
    return esc('G', [pos])




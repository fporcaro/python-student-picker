from wheel_view_model import WheelViewModel
import terminal


class TerminalWheelView:
    def __init__(self, wheel_view_model: WheelViewModel, lines_to_display=5, starting_index=0):
        self.wheel_view_model = wheel_view_model
        self.lines_to_display = lines_to_display
        self.starting_index = starting_index
        self.wheel_view_model.current_item_index = starting_index
        self.num_items_either_side = self.lines_to_display // 2
        self.item_index_range = range(self.num_items_either_side * -1, self.num_items_either_side + 1)
        self.colors = [terminal.fg.rgb(64, 64, 64), terminal.fg.rgb(128, 128, 128), terminal.fg.green, terminal.fg.rgb(128, 128, 128), terminal.fg.rgb(64, 64, 64)]

    def print_wheel(self):
        terminal.cursor_previous_line(self.lines_to_display)
        for line_index in self.item_index_range:
            line_text = self.wheel_view_model.get_displayed_line_item(line_index=line_index)
            terminal.erase_entire_line()
            terminal.write(self.colors[line_index+self.num_items_either_side] + line_text)
            terminal.cursor_next_line()
        terminal.write(terminal.fg.white)

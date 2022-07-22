from typing import List

import terminal
import logging


class Wheel:
    def __init__(self, line_items: List[str]):
        self.line_items = line_items
        self.current_item_index = 0

    def increment_wheel(self):
        self.current_item_index = get_next_index(self.line_items, self.current_item_index)

    def get_current_line_item(self):
        return self.line_items[self.current_item_index]

    def get_displayed_line_item(self, line_index):
        """
        Returns the line item text of the item based on line_index
        :param line_index:  0 for the currently selected item, -1 for the item just above it, 1 for the item just below the selected item, and so on.
        :return:
        """
        if line_index < 0:
            index_function = get_previous_index
        if line_index > 0:
            index_function = get_next_index
        else:
            index_function = None

        item_index = self.current_item_index
        for count in range(abs(line_index)):
            item_index = index_function(line_items=self.line_items, current_index=item_index)
        return self.line_items[self.current_item_index]


def get_next_index(line_items, current_index):
    return (current_index + 1) % len(line_items)


def get_previous_index(line_items, current_index):
    previous_index = current_index - 1
    if previous_index < 0:
        previous_index = len(line_items)
    return previous_index


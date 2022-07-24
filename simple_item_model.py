import random


class SimpleItemModel:
    def __init__(self, items, pop_quiz_item):
        self.main_items = items
        self.featured_item = None
        self.pop_quiz_item = pop_quiz_item
        self.pop_quiz_item_enabled = False
        self.current_items = []
        self.build_current_items()

    def select_item(self):
        if self.featured_item is not None:
            selected_item = self.featured_item
            self.featured_item = None
        else:
            selected_item = random.choices(self.current_items)[0]
        self.selected_item(selected_item)
        return selected_item

    def selected_item(self, item):
        print(f'Selected item: {item}')

    def toggle_pop_quiz_item_enabled(self):
        self.set_pop_quiz_item_enabled(not self.pop_quiz_item_enabled)
        return self.pop_quiz_item_enabled

    def set_pop_quiz_item_enabled(self, is_enabled):
        self.pop_quiz_item_enabled = is_enabled
        self.build_current_items()

    def peek_random_items(self, quantity=1):
        return random.choices(self.current_items, k=quantity)

    def build_current_items(self):
        """
        Build the full set of available items including any available main items and the pop quiz item if enabled.
        :return:
        """
        self.current_items = self.main_items
        if self.pop_quiz_item_enabled:
            self.current_items.append(self.pop_quiz_item)

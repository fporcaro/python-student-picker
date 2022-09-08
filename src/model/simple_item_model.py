import random


class SimpleItemModel:
    def __init__(self, main_items, pop_quiz_item, pop_quiz_item_enabled=False, featured_item=None):
        self.main_items = main_items.copy()
        self.featured_item = featured_item
        self.pop_quiz_item = pop_quiz_item
        self.pop_quiz_item_enabled = pop_quiz_item_enabled
        # Current items represent the set of available items from which things are selected.  This includes the pop quiz item
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
        pass

    def toggle_pop_quiz_item_enabled(self):
        self.set_pop_quiz_item_enabled(not self.pop_quiz_item_enabled)
        return self.pop_quiz_item_enabled

    def set_pop_quiz_item_enabled(self, is_enabled):
        self.pop_quiz_item_enabled = is_enabled
        self.build_current_items()

    def peek_random_items(self, quantity=1):
        random_item_quantity = min([quantity, len(self.current_items)])
        if random_item_quantity == 0:
            return []
        return random.choices(self.current_items, k=random_item_quantity)

    def get_items_remaining_count(self):
        return len(self.current_items)

    def build_current_items(self):
        """
        Build the full set of available items including any available main items and the pop quiz item if enabled.
        :return:
        """
        self.current_items = self.main_items.copy()
        if self.pop_quiz_item_enabled:
            self.current_items.append(self.pop_quiz_item)

    def undo(self):
        """
        Undo the last selection.  If the model changes when selecting an item, make the last
        selection like it didn't happen
        :return:
        """
        # The simple model doesn't modify it's items, so do nothing
        pass
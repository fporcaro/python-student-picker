import random


class SimpleItemModel:
    def __init__(self, items, weights=None):
        self.weights = weights
        self.items = items

    def select_item(self):
        selected_item = random.choices(self.items, weights=self.weights)[0]
        self.selected_item(selected_item)
        return selected_item

    def selected_item(self, item):
        print(f'Selected item: {item}')

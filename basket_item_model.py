from simple_item_model import SimpleItemModel


class BasketItemModel(SimpleItemModel):
    def __init__(self, items, weights=None):
        super().__init__(items, weights)
        self.original_items = items.copy()
        if weights is not None:
            self.original_weights = weights.copy()
        else:
            self.original_weights = None

    def selected_item(self, item):
        """Remove the selected item from the basket"""
        index = self.items.index(item)
        self.items.remove(item)
        if self.weights is not None:
            self.weights.pop(index)

    def reset_basket(self):
        self.items = self.original_items.copy()
        if self.original_weights is not None:
            self.weights = self.original_weights.copy()

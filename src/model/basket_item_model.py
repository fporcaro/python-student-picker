from src.model.simple_item_model import SimpleItemModel


class BasketItemModel(SimpleItemModel):
    def __init__(self, main_items, pop_quiz_item, pop_quiz_item_enabled=False, featured_item=None, previously_selected_items=None):
        if previously_selected_items is None:
            self.previously_selected_items = []
        else:
            self.previously_selected_items = previously_selected_items
        super().__init__(main_items=main_items, pop_quiz_item=pop_quiz_item,
                         pop_quiz_item_enabled=pop_quiz_item_enabled, featured_item=featured_item)
        # super will call self.build_current_items()

    def selected_item(self, item):
        """Remove the selected item from the basket"""
        self.current_items.remove(item)
        self.previously_selected_items.append(item)

    def select_item(self):
        if len(self.current_items) == 0:
            self.reset_basket()
        return super().select_item()

    def reset_basket(self):
        self.previously_selected_items = []
        self.build_current_items()

    def build_current_items(self):
        super(BasketItemModel, self).build_current_items()
        for item in self.previously_selected_items:
            self.current_items.remove(item)

    def undo(self):
        last_item = self.previously_selected_items.pop()
        self.current_items.append(last_item)
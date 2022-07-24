from simple_item_model import SimpleItemModel


class BasketItemModel(SimpleItemModel):
    def __init__(self, main_items, pop_quiz_item):
        super().__init__(items=main_items, pop_quiz_item=pop_quiz_item)
        self.original_main_items = main_items.copy()

    def selected_item(self, item):
        """Remove the selected item from the basket"""
        self.main_items.remove(item)

    def reset_basket(self):
        self.main_items = self.original_main_items.copy()
        self.build_current_items()

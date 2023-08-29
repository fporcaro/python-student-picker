
class ItemModel:
    def __init__(self, number, name, previously_selected=False, enabled=False, featured=False):
        self.number = number
        self.name = name
        self.previously_selected = previously_selected
        self.enabled = enabled
        self.featured = featured

    def __lt__(self, other):
        return self.number < other.number



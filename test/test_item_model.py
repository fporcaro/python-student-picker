import unittest

from src.model.item_model import ItemModel


class MyTestCase(unittest.TestCase):
    def test_lt(self):
        item_p = ItemModel("P", "Pop Quiz")
        item_one = ItemModel("1", "Item One")
        item_two = ItemModel("2", "Item Two")
        self.assertTrue(item_one < item_two)
        self.assertTrue(item_one < item_p)
        self.assertTrue(item_two < item_p)


if __name__ == '__main__':
    unittest.main()

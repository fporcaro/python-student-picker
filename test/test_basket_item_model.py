import unittest
from basket_item_model import BasketItemModel


class BasketItemModelTestCase(unittest.TestCase):
    def test_basket(self):
        items = ['one', 'two', 'three']
        basket_item_model = BasketItemModel(items=items.copy())
        item = basket_item_model.select_item()
        self.assertIn(item, items)
        self.assertEqual(2, len(basket_item_model.items))

        item2 = basket_item_model.select_item()
        self.assertIn(item2, items)
        self.assertEqual(1, len(basket_item_model.items))

        item3 = basket_item_model.select_item()
        self.assertIn(item3, items)
        self.assertEqual(0, len(basket_item_model.items))

        basket_item_model.reset_basket()
        self.assertEqual(3, len(basket_item_model.items))


if __name__ == '__main__':
    unittest.main()

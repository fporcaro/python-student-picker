import unittest
from basket_item_model import BasketItemModel


class BasketItemModelTestCase(unittest.TestCase):
    def test_basket(self):
        items = ['one', 'two', 'three']
        basket_item_model = BasketItemModel(main_items=items.copy(), pop_quiz_item="Pop Quiz")
        basket_item_model.set_pop_quiz_item_enabled(False)
        item = basket_item_model.select_item()
        self.assertIn(item, items)
        self.assertEqual(2, len(basket_item_model.current_items))

        item2 = basket_item_model.select_item()
        self.assertIn(item2, items)
        self.assertEqual(1, len(basket_item_model.current_items))

        item3 = basket_item_model.select_item()
        self.assertIn(item3, items)
        self.assertEqual(0, len(basket_item_model.current_items))

        basket_item_model.reset_basket()
        self.assertEqual(3, len(basket_item_model.current_items))

    def test_basket_with_pop_quiz_enabled(self):
        items = ['one', 'two', 'three']
        pop_quiz_item = "Pop Quiz"
        basket_item_model = BasketItemModel(main_items=items.copy(), pop_quiz_item=pop_quiz_item)
        basket_item_model.set_pop_quiz_item_enabled(True)
        item = basket_item_model.select_item()
        self.assertTrue(item in items or item == pop_quiz_item)
        self.assertEqual(3, len(basket_item_model.current_items))

        item2 = basket_item_model.select_item()
        self.assertTrue(item2 in items or item2 == pop_quiz_item)
        self.assertEqual(2, len(basket_item_model.current_items))

        item3 = basket_item_model.select_item()
        self.assertTrue(item3 in items or item3 == pop_quiz_item)
        self.assertEqual(1, len(basket_item_model.current_items))

        item4 = basket_item_model.select_item()
        self.assertTrue(item4 in items or item4 == pop_quiz_item)
        self.assertEqual(0, len(basket_item_model.current_items))

        basket_item_model.reset_basket()
        self.assertEqual(4, len(basket_item_model.current_items))


if __name__ == '__main__':
    unittest.main()

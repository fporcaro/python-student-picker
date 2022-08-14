import unittest
from src.model.simple_item_model import SimpleItemModel

class TestSimpleItemModel(unittest.TestCase):
    def test_standard_select_item(self):
        items = ['one', 'two', 'three']
        simple_item_model = SimpleItemModel(main_items=items.copy(), pop_quiz_item="Pop Quiz")
        simple_item_model.set_pop_quiz_item_enabled(False)
        item = simple_item_model.select_item()
        self.assertIn(item, items)
        self.assertEqual(3, len(simple_item_model.current_items))

    def test_pop_quiz_enabled(self):
        items = ['one', 'two', 'three']
        simple_item_model = SimpleItemModel(main_items=items.copy(), pop_quiz_item="Pop Quiz")
        simple_item_model.set_pop_quiz_item_enabled(True)
        item = simple_item_model.select_item()
        self.assertIn(item, simple_item_model.current_items)
        self.assertEqual(4, len(simple_item_model.current_items))

    def test_featured_item_no_pop_quiz(self):
        items = ['one', 'two', 'three']
        simple_item_model = SimpleItemModel(main_items=items.copy(), pop_quiz_item="Pop Quiz")
        simple_item_model.set_pop_quiz_item_enabled(False)
        simple_item_model.featured_item = 'one'
        item = simple_item_model.select_item()
        self.assertEqual('one', item)
        self.assertEqual(3, len(simple_item_model.current_items))

    def test_featured_item_pop_quiz(self):
        items = ['one', 'two', 'three']
        pop_quiz_item = "Pop Quiz"
        simple_item_model = SimpleItemModel(main_items=items.copy(), pop_quiz_item=pop_quiz_item)
        simple_item_model.set_pop_quiz_item_enabled(True)
        simple_item_model.featured_item = pop_quiz_item
        item = simple_item_model.select_item()
        self.assertEqual(pop_quiz_item, item)
        self.assertEqual(4, len(simple_item_model.current_items))


if __name__ == '__main__':
    unittest.main()

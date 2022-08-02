import unittest
from item_reveal_view import ItemRevealView


class MyTestCase(unittest.TestCase):
    def test_calculate_decaying_time_slices(self):
        initial = 5
        slice_count = 15
        item_reveal_view = ItemRevealView(default_initial_duration=initial)
        slices = item_reveal_view.calculate_decaying_time_slices(number_of_slices=slice_count)
        self.assertEqual(slice_count, len(slices))
        self.assertEqual(initial, slices[0])

    def test_randomize_letters(self):
        source = 'Frank'
        item_reveal_view = ItemRevealView(default_initial_duration=1)
        randomized = item_reveal_view.randomize_letters(source=source)
        self.assertEqual(len(source), len(randomized))
        self.assertIn(('F', 1), randomized)


if __name__ == '__main__':
    unittest.main()

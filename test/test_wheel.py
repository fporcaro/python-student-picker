import unittest
from wheel_view_model import get_next_index


class WheelTestCase(unittest.TestCase):
    def test_wrap_around(self):
        items = ["one", "two", "three"]
        current_index = 0
        next_index = get_next_index(line_items=items, current_index=current_index)
        self.assertEqual(1, next_index)
        current_index = next_index
        next_index = get_next_index(line_items=items, current_index=current_index)
        self.assertEqual(2, next_index)
        current_index = next_index
        next_index = get_next_index(line_items=items, current_index=current_index)
        self.assertEqual(0, next_index)


if __name__ == '__main__':
    unittest.main()

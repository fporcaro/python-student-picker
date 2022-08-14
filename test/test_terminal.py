import unittest
from src.services.terminal import terminal


class TerminalTestCase(unittest.TestCase):
    def test_no_params(self):
        self.assertEqual(f'{terminal.ESC_PREFIX}K', terminal.esc('K'))

    def test_one_params(self):
        one = 10
        self.assertEqual(f'{terminal.ESC_PREFIX}{one}K', terminal.esc('K', [one]))

    def test_two_params(self):
        one = 10
        two = 20
        self.assertEqual(f'{terminal.ESC_PREFIX}{one};{two}K', terminal.esc('K', [one, two]))


if __name__ == '__main__':
    unittest.main()

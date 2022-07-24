import msvcrt
import random

from basket_item_model import BasketItemModel
from item_reveal_view import ItemRevealView
from simple_item_model import SimpleItemModel
import terminal

MODE_QUICK = 'Quick'
MODE_DRAMATIC = 'Dramatic'
MODEL_LIST = 'List'
MODEL_BASKET = 'Basket'

COMMAND_CHAR_EXIT = b'x'
COMMAND_CHAR_LIST_MODE = b'l'
COMMAND_CHAR_BASKET_MODE = b'b'
COMMAND_CHAR_POP_QUIZ_TOGGLE = b'p'
COMMAND_CHAR_FEATURE_ITEM = b'f'
COMMAND_CHAR_QUICK_MODE = b'q'
COMMAND_CHAR_DRAMATIC_MODE = b'd'
COMMAND_CHAR_SELECT_ITEM = b' '


class SuperRandomizerManager:
    def __init__(self, list_model: SimpleItemModel, basket_model: BasketItemModel, pop_quiz_item):
        self.list_model = list_model
        self.basket_model = basket_model
        self.pop_quiz_item = pop_quiz_item
        self.mode = MODE_DRAMATIC
        self.current_model_type = MODEL_LIST
        self.current_model = self.list_model
        self.feature_item = None
        self.item_reveal_view = ItemRevealView()

    def handle_command_character(self, character):
        command_character = character.lower()
        if command_character == COMMAND_CHAR_EXIT:
            self.exit()
        elif command_character == COMMAND_CHAR_POP_QUIZ_TOGGLE:
            self.list_model.toggle_pop_quiz_item_enabled()
            self.basket_model.toggle_pop_quiz_item_enabled()
            self.write_pop_quiz()
        elif command_character == COMMAND_CHAR_DRAMATIC_MODE:
            self.mode = MODE_DRAMATIC
            self.write_mode()
        elif command_character == COMMAND_CHAR_QUICK_MODE:
            self.mode = MODE_QUICK
            self.write_mode()
        elif command_character == COMMAND_CHAR_LIST_MODE:
            self.current_model_type = MODEL_LIST
            self.current_model = self.list_model
            self.write_model()
        elif command_character == COMMAND_CHAR_BASKET_MODE:
            self.current_model_type = MODEL_BASKET
            self.current_model = self.basket_model
            self.write_model()
        elif command_character == COMMAND_CHAR_SELECT_ITEM:
            self.select_and_display_item()
        # elif command_character == COMMAND_CHAR_FEATURE_ITEM:
        #     feature_item_index = msvcrt.
        else:
            self.write_key(key=f"Unknown command {command_character}")

    def exit(self):
        exit(0)

    def start(self):
        terminal.erase_in_display(function=2)
        self.write_mode()
        self.write_model()
        self.write_pop_quiz()

    def write_mode(self):
        terminal.set_cursor_position(1, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Mode: {self.mode}")

    def write_model(self):
        terminal.set_cursor_position(2, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Model: {self.current_model_type}")

    def write_pop_quiz(self):
        terminal.set_cursor_position(3, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Pop Quiz Enabled: {self.list_model.pop_quiz_item_enabled}")

    def select_and_display_item(self):
        terminal.set_cursor_position(6, 1)
        selected_item = self.current_model.select_item()
        if self.mode == MODE_DRAMATIC:
            peek_item_count = random.uniform(2, 4)
            peek_items = self.current_model.peek_random_items(quantity=2)
            self.item_reveal_view.reveal_value_dramatic(selected_item, peek_values=peek_items)
        elif self.mode == MODE_QUICK:
            self.item_reveal_view.reveal_value(value=selected_item)

    def write_key(self, key):
        terminal.set_cursor_position(10, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Received key: {key}")

    def process_input_loop(self):
        key = msvcrt.getch()
        self.write_key(key)
        while key != COMMAND_CHAR_EXIT:
            self.handle_command_character(character=key)
            key = msvcrt.getch()
            self.write_key(key)


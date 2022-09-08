import msvcrt
import random

from src.model.basket_item_model import BasketItemModel
from src.model.student_picker_manager_event_handler import StudentPickerManagerEventHandler
from src.view.item_reveal_view import ItemRevealView
from src.model.simple_item_model import SimpleItemModel
from src.services.terminal import terminal
import logging

ROW_MODEL_STATUS = 11

ROW_INPUT_KEY = 10
ROW_ITEM = 7
ROW_ITEMS_REMAINING = 4
ROW_POP_QUIZ = 3
ROW_MODEL = 2
ROW_MODE = 1

DEFAULT_MAX_PEEK_ITEMS = 4

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
COMMAND_CHAR_SHOW_MODEL = b'm'
COMMAND_CHAR_UNDO = b'u'
COMMAND_CHAR_RELOAD = b'r'


class StudentPickerManager:
    def __init__(self, master_items, list_model: SimpleItemModel, basket_model: BasketItemModel, mode=MODE_DRAMATIC,
                 current_model_type=MODEL_LIST, max_peek_items=DEFAULT_MAX_PEEK_ITEMS, featured_item=None,
                 event_handler: StudentPickerManagerEventHandler=None):
        self.master_items = master_items # The list of items loaded from the source.  State of previous selection and featured status only valid upon loading
        self.list_model = list_model
        self.basket_model = basket_model
        self.mode = mode
        self.set_current_model_type(current_model_type)
        self.featured_item = featured_item
        self.item_reveal_view = ItemRevealView()
        self.max_peek_items = max_peek_items
        self.should_show_model = False
        self.event_handler = event_handler

    def handle_command_character(self, character):
        command_character = character.lower()
        if command_character == COMMAND_CHAR_EXIT:
            self.exit()
        elif command_character == COMMAND_CHAR_POP_QUIZ_TOGGLE:
            self.list_model.toggle_pop_quiz_item_enabled()
            self.basket_model.toggle_pop_quiz_item_enabled()
            self.show_pop_quiz()
        elif command_character == COMMAND_CHAR_DRAMATIC_MODE:
            self.mode = MODE_DRAMATIC
            self.show_mode()
        elif command_character == COMMAND_CHAR_QUICK_MODE:
            self.mode = MODE_QUICK
            self.show_mode()
        elif command_character == COMMAND_CHAR_LIST_MODE:
            self.set_current_model_type(MODEL_LIST)
            self.show_model()
            self.show_items_remaining()
        elif command_character == COMMAND_CHAR_BASKET_MODE:
            self.set_current_model_type(MODEL_BASKET)
            self.show_model()
            self.show_items_remaining()
        elif command_character == COMMAND_CHAR_SELECT_ITEM:
            self.select_and_show_item()
            self.show_items_remaining()
        elif command_character == COMMAND_CHAR_SHOW_MODEL:
            self.should_show_model = not self.should_show_model
        elif command_character == COMMAND_CHAR_UNDO:
            self.current_model.undo()
        # elif command_character == COMMAND_CHAR_FEATURE_ITEM:
        #     feature_item_index = msvcrt.
        else:
            self.show_key(key=f"Unknown command {command_character}")

    def set_current_model_type(self, model_type):
        self.current_model_type = model_type
        if model_type == MODEL_LIST:
            self.current_model = self.list_model
        elif model_type == MODEL_BASKET:
            self.current_model = self.basket_model

    def exit(self):
        exit(0)

    def start(self):
        terminal.erase_in_display(function=2)
        self.show_mode()
        self.show_model()
        self.show_pop_quiz()
        self.show_items_remaining()

    def show_mode(self):
        terminal.set_cursor_position(ROW_MODE, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Mode: {self.mode}")

    def show_model(self):
        terminal.set_cursor_position(ROW_MODEL, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Model: {self.current_model_type}")

    def show_pop_quiz(self):
        terminal.set_cursor_position(ROW_POP_QUIZ, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Pop Quiz Enabled: {self.list_model.pop_quiz_item_enabled}")

    def show_items_remaining(self):
        terminal.set_cursor_position(ROW_ITEMS_REMAINING, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Items Remaining: {self.current_model.get_items_remaining_count()}")

    def select_and_show_item(self):
        terminal.set_cursor_position(ROW_ITEM, 1)
        selected_item = self.current_model.select_item()
        if len(self.current_model.current_items) == 0 or self.mode == MODE_QUICK:
            self.item_reveal_view.reveal_value(value=selected_item)
        elif self.mode == MODE_DRAMATIC:
            peek_item_count = int(random.uniform(1, self.max_peek_items))
            peek_items = self.current_model.peek_random_items(quantity=peek_item_count)
            self.item_reveal_view.reveal_value_dramatic(selected_item, peek_values=peek_items)
        else:
            logging.error(f"Unexpected select and display: {self.current_model}")
            exit(2)
        if self.event_handler is not None:
            self.event_handler.handle_item_selected(selected_item, self)

    def show_key(self, key):
        terminal.set_cursor_position(ROW_INPUT_KEY, 1)
        terminal.erase_to_end_of_line()
        terminal.write(f"Received key: {key}")

    def show_model_status(self):
        terminal.set_cursor_position(ROW_MODEL_STATUS, 1)
        terminal.erase_to_end_of_line()
        if self.should_show_model:
            terminal.write(f"Basket Model: {self.basket_model.current_items}")
        terminal.set_cursor_position(ROW_MODEL_STATUS + 1, 1)
        terminal.erase_to_end_of_line()
        if self.should_show_model:
            terminal.write(f"Basket Model Selected: {self.basket_model.previously_selected_items}")

    def process_input_loop(self):
        key = msvcrt.getch()
        self.show_key(key)
        while key != COMMAND_CHAR_EXIT:
            self.handle_command_character(character=key)
            self.show_model_status()
            key = msvcrt.getch()
            self.show_key(key)


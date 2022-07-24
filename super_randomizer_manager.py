

MODE_QUICK = 'quick'
MODE_DRAMATIC = 'dramatic'
MODEL_LIST = 'list'
MODEL_BASKET = 'basket'

COMMAND_CHAR_QUIT = 'q'
COMMAND_CHAR_LIST_MODE = 'l'
COMMAND_CHAR_BASKET_MODE = 'b'
COMMAND_CHAR_POP_QUIZ_TOGGLE = 'p'
COMMAND_CHAR_FEATURE_ITEM = 'f'


class SuperRandomizerManager:
    def __init__(self, list_model, basket_model, pop_quiz_item):
        self.list_model = list_model
        self.basket_model = basket_model
        self.pop_quiz_item = pop_quiz_item
        self.mode = MODE_DRAMATIC
        self.current_model_type = MODEL_LIST
        self.current_model = self.list_model
        self.pop_quiz_enabled = True
        self.feature_item = None

    def handle_command_character(self, character):
        if character == ''

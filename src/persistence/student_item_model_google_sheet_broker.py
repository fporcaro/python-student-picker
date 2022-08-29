from src.model.student_picker_manager_event_handler import StudentPickerManagerEventHandler
from src.persistence.item_factory import ItemFactory
from src.persistence.student_picker_sheet import StudentPickerSheet, ITEM_COLUMN_ENABLED, ITEM_COLUMN_NAME, ITEM_COLUMN_PREVIOUSLY_SELECTED
from src.model.simple_item_model import SimpleItemModel
from src.model.basket_item_model import BasketItemModel
from src.model.student_picker_manager import StudentPickerManager, MODEL_LIST, MODEL_BASKET
import logging


class StudentPickerManagerGoogleSheetBroker(StudentPickerManagerEventHandler):
    def __init__(self, student_picker_sheet: StudentPickerSheet):
        self.student_picker_sheet = student_picker_sheet

    def create_manager_from_sheet(self):
        mode = self.student_picker_sheet.read_mode()
        model_type = self.student_picker_sheet.read_model()
        pop_quiz_item = self.student_picker_sheet.read_pop_quiz_item()
        student_items = self.student_picker_sheet.read_student_items()
        simple_item_model = self.create_simple_item_model_from_student_items(student_items, pop_quiz_item=pop_quiz_item)
        basket_item_model = self.create_basket_item_model_from_student_items(student_items, pop_quiz_item=pop_quiz_item)
        return StudentPickerManager(master_items=student_items, list_model=simple_item_model,
                                    basket_model=basket_item_model, mode=mode, current_model_type=model_type,
                                    event_handler=self)


    def create_simple_item_model_from_student_items(self, student_items, pop_quiz_item):
        items = []
        for student_item in student_items:
            if student_item.enabled:
                items.append(student_item.name)
        pop_quiz_value = pop_quiz_item.name
        pop_quiz_enabled = pop_quiz_item.enabled
        return SimpleItemModel(main_items=items, pop_quiz_item=pop_quiz_value, pop_quiz_item_enabled=pop_quiz_enabled)

    def create_basket_item_model_from_student_items(self, student_items, pop_quiz_item):
        main_items = []
        previously_selected_items = []
        for student_item in student_items:
            current_item = student_item.name
            if student_item.enabled:
                main_items.append(current_item)
                if student_item.previously_selected:
                    previously_selected_items.append(current_item)
        pop_quiz_value = pop_quiz_item.name
        pop_quiz_enabled = pop_quiz_item.enabled
        return BasketItemModel(main_items=main_items, pop_quiz_item=pop_quiz_value,
                               pop_quiz_item_enabled=pop_quiz_enabled, featured_item=None,
                               previously_selected_items=previously_selected_items)

    def write_student_picker_state(self, student_picker_manager: StudentPickerManager):
        self.student_picker_sheet.write_mode(student_picker_manager.mode)
        self.write_current_model_type(student_picker_manager)
        self.write_student_items(student_picker_manager)

    def write_current_model_type(self, student_picker_manager):
        if student_picker_manager.current_model.__class__ == BasketItemModel:
            self.student_picker_sheet.write_model(MODEL_BASKET)
        elif student_picker_manager.current_model.__class__ == SimpleItemModel:
            self.student_picker_sheet.write_model(MODEL_LIST)
        else:
            logging.error(f"Unknown model type: {student_picker_manager.current_model}")

    def write_student_items(self, student_picker_manager: StudentPickerManager):
        items = student_picker_manager.master_items
        basket_item_model = student_picker_manager.basket_model
        for item in items:
            item.previously_selected = item.name in basket_item_model.previously_selected_items
        self.student_picker_sheet.write_student_items(student_items=items)

    def handle_item_selected(self, selected_item, student_picker_manager: StudentPickerManager):
        self.write_student_items(student_picker_manager=student_picker_manager)

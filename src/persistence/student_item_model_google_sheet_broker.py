from src.persistence.student_picker_sheet import StudentPickerSheet, ITEM_COLUMN_ENABLED, ITEM_COLUMN_NAME, ITEM_COLUMN_PREVIOUSLY_SELECTED
from src.model.simple_item_model import SimpleItemModel
from src.model.basket_item_model import BasketItemModel
from src.model.student_picker_manager import StudentPickerManager


class StudentPickerManagerGoogleSheetBroker:
    def __init__(self, student_picker_sheet: StudentPickerSheet):
        self.student_picker_sheet = student_picker_sheet

    def create_manager_from_sheet(self):
        mode = self.student_picker_sheet.read_mode()
        model_type = self.student_picker_sheet.read_model()
        pop_quiz_item = self.student_picker_sheet.read_pop_quiz_item()
        student_items = self.student_picker_sheet.read_student_items()
        simple_item_model = self.create_simple_item_model_from_student_items(student_items, pop_quiz_item=pop_quiz_item)
        basket_item_model = self.create_basket_item_model_from_student_items(student_items, pop_quiz_item=pop_quiz_item)
        return StudentPickerManager(list_model=simple_item_model, basket_model=basket_item_model, mode=mode, current_model_type=model_type)


    def cell_value_as_bool(self, cell_value):
        return cell_value.lower() == 'x'

    def boolean_as_cell_value(self, boolean_value):
        if boolean_value:
            return 'x'
        return ''

    def create_simple_item_model_from_student_items(self, student_items, pop_quiz_item):
        items = []
        for student_item in student_items:
            if self.cell_value_as_bool(student_item.get(ITEM_COLUMN_ENABLED, '')):
                items.append(student_item.get(ITEM_COLUMN_NAME))
        pop_quiz_value = pop_quiz_item.get(ITEM_COLUMN_NAME)
        pop_quiz_enabled = self.cell_value_as_bool(pop_quiz_item.get(ITEM_COLUMN_ENABLED, ''))
        return SimpleItemModel(main_items=items, pop_quiz_item=pop_quiz_value, pop_quiz_item_enabled=pop_quiz_enabled)

    def create_basket_item_model_from_student_items(self, student_items, pop_quiz_item):
        main_items = []
        previously_selected_items = []
        for student_item in student_items:
            current_item = student_item.get(ITEM_COLUMN_NAME)
            if self.cell_value_as_bool(student_item.get(ITEM_COLUMN_ENABLED, '')):
                main_items.append(current_item)
                if self.cell_value_as_bool((student_item.get(ITEM_COLUMN_PREVIOUSLY_SELECTED, ''))):
                    previously_selected_items.append(current_item)
        pop_quiz_value = pop_quiz_item.get(ITEM_COLUMN_NAME)
        pop_quiz_enabled = self.cell_value_as_bool(pop_quiz_item.get(ITEM_COLUMN_ENABLED, ''))
        return BasketItemModel(main_items=main_items, pop_quiz_item=pop_quiz_value,
                               pop_quiz_item_enabled=pop_quiz_enabled, featured_item=None,
                               previously_selected_items=previously_selected_items)

    def save_student_item_model(self, student_item_model):
        pass
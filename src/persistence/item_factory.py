from src.model.item_model import ItemModel
from src.persistence.student_picker_sheet import ITEM_COLUMN_ENABLED, ITEM_COLUMN_PREVIOUSLY_SELECTED, ITEM_COLUMN_NAME, ITEM_COLUMN_NUMBER, ITEM_COLUMN_FEATURED


class ItemFactory:
    @staticmethod
    def create_item_model(item_dict):
        return ItemModel(item_dict.get(ITEM_COLUMN_NUMBER), item_dict.get(ITEM_COLUMN_NAME),
                         item_dict.get(ItemFactory.cell_value_as_bool()),
                         item_dict.get(ItemFactory.cell_value_as_bool()),
                         item_dict.get(ItemFactory.cell_value_as_bool()))

    @staticmethod
    def cell_value_as_bool(cell_value):
        return cell_value.lower() == 'x'

    @staticmethod
    def boolean_as_cell_value(boolean_value):
        if boolean_value:
            return 'x'
        return ''

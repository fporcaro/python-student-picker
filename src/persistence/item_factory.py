from src.model.item_model import ItemModel

ITEM_COLUMN_NUMBER = 'number'
ITEM_COLUMN_NAME = 'name'
ITEM_COLUMN_PREVIOUSLY_SELECTED = 'previously_selected'
ITEM_COLUMN_ENABLED = 'enabled'
ITEM_COLUMN_FEATURED = 'featured'
ITEM_COLUMN_HEADERS = [ITEM_COLUMN_NUMBER, ITEM_COLUMN_NAME, ITEM_COLUMN_PREVIOUSLY_SELECTED, ITEM_COLUMN_ENABLED, ITEM_COLUMN_FEATURED]

class ItemFactory:
    @staticmethod
    def create_item_model(item_dict):
        number = item_dict.get(ITEM_COLUMN_NUMBER)
        name = item_dict.get(ITEM_COLUMN_NAME)
        previously_selected = ItemFactory.cell_value_as_bool(item_dict.get(ITEM_COLUMN_PREVIOUSLY_SELECTED, ''))
        enabled = ItemFactory.cell_value_as_bool(item_dict.get(ITEM_COLUMN_ENABLED, ''))
        featured = ItemFactory.cell_value_as_bool(item_dict.get(ITEM_COLUMN_FEATURED, ''))
        return ItemModel(number=number, name=name,
                         previously_selected=previously_selected,
                         enabled=enabled,
                         featured=featured)

    @staticmethod
    def create_dict_from_item_model(item_model):
        return {
            ITEM_COLUMN_NAME: item_model.name,
            ITEM_COLUMN_NUMBER: item_model.number,
            ITEM_COLUMN_PREVIOUSLY_SELECTED: ItemFactory.boolean_as_cell_value(item_model.previously_selected),
            ITEM_COLUMN_ENABLED: ItemFactory.boolean_as_cell_value(item_model.enabled),
            ITEM_COLUMN_FEATURED: ItemFactory.boolean_as_cell_value(item_model.featured)
        }

    @staticmethod
    def cell_value_as_bool(cell_value):
        return cell_value.lower() == 'x'

    @staticmethod
    def boolean_as_cell_value(boolean_value):
        if boolean_value:
            return 'x'
        return ''

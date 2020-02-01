from sheets_todo_list.mapping import mapping
from sheets_todo_list.sheet import Sheet


class InsertContent:
    def __init__(self):
        self._sheet = Sheet.initailize()

    def to_the_top(self, content, column_name):
        """
            Add content to top of list and push all items that are not connected to the block in the top to make them connected
        """
        cell_list = self._sheet.range(mapping[column_name]['range'])

        # check if there's still space left and clean up the cells
        has_empty = False
        reshufled_list = [content]
        for i in cell_list:
            if i.value == "":
                has_empty=True
            else:
                reshufled_list.append(i.value)
                i.value = ''

        if not has_empty:
            raise Exception("No space left in the inbox clean it up first!")

        self._sheet.update_cells(cell_list)
        the_range = f'{mapping[column_name]["top"]}:{mapping[column_name]["col"]}{2 + len(reshufled_list)}'
        cell_list = self._sheet.range(the_range)

        for indice, i in enumerate(cell_list):
            i.value = reshufled_list[indice]

        self._sheet.update_cells(cell_list)
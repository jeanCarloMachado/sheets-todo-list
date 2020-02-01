from sheets_todo_list.mapping import Mapping
from sheets_todo_list.sheet import Sheet
from datetime import date, timedelta


class Done:
    def __init__(self):
        self._sheet = Sheet.initailize()
        self._mapping = Mapping()

    def clean_today(self):

        #clean done today
        cell_list = self._sheet.range(self._mapping.column_meta('done', 'range'))

        yesterday = date.today() - timedelta(days=1)
        yesterday_str = yesterday.strftime("%a %Y-%-m-%-d")
        yesterday_cell = self._sheet.find(yesterday_str)

        col_letter = chr(64 + yesterday_cell.col)
        first_position = yesterday_cell.row + 1
        last_position = first_position+(len(cell_list)-1)
        range = f"{col_letter}{first_position}:{col_letter}{last_position}"
        log_cell_list = self._sheet.range(range)
        for i, v in enumerate(log_cell_list):
            v.value = cell_list[i].value

        for i in cell_list:
            i.value = ""

        #commit changes
        self._sheet.update_cells(cell_list)
        self._sheet.update_cells(log_cell_list)


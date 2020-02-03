from sheets_todo_list.mapping import Mapping
from sheets_todo_list.sheet import Sheet
from sheets_todo_list.column import Column
from itertools import takewhile

class Projects:
    def __init__(self):
        self._sheet = Sheet.initailize()
        self._mapping = Mapping()

    def sort(self):
        #take only the relevant part of the projects section
        start_col = self._mapping.column_meta('projects', 'start_col')

        projects_line = self.get_project_line()
        for indice in list(range(0, len(projects_line))):
            projects_line = self.get_project_line()
            remainer_list = projects_line[indice:]
            print(f"Remainder list {remainer_list}")
            minimal_val = min(remainer_list)
            min_val_index = projects_line.index(minimal_val)
            print(f"Min val index {min_val_index}")
            if minimal_val < projects_line[indice]:
                print(f"Swap values from indice {Column(start_col).increment_indice(indice)} to indice {Column(start_col).increment_indice(min_val_index)}")
                first_col = Column(start_col).increment_indice(indice)
                first = self._sheet.range(f'{first_col}1:{first_col}10')

                second_col = Column(start_col).increment_indice(min_val_index)
                second = self._sheet.range(f'{second_col}1:{second_col}10')

                for indice, value in enumerate(first):
                    first_value = first[indice].value
                    first[indice].value = second[indice].value
                    second[indice].value = first_value

                    self._sheet.update_cells(first)
                    self._sheet.update_cells(second)



    def get_project_line(self):
        sort_line = self._sheet.range(self._mapping.column_meta('projects', 'sort_line'))
        sort_line_values = list(map(lambda x: x.value, sort_line))
        sort_line_trimmed_right = list(takewhile(lambda x: x != '', sort_line_values))
        projects_line = sort_line_trimmed_right
        return projects_line


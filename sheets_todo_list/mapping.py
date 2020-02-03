
class Mapping:
    def __init__(self):
        self._content = {
            'inbox': {
                'col': 'A',
                'top': 'A3',
                'range': 'A3:A20'
            },
            'today': {
                'col': 'B',
                'top': 'B3',
                'range': 'B3:B20'
            },
            'done': {
                'col': 'C',
                'top': 'C3',
                'range': 'C3:C20'
            },
            'projects': {
                'start_col': 'F',
                'sort_line': 'F1:Z1',
                'range': 'F1:Z10'
            }
        }
    def column_meta(self, column_name, meta):
        return self._content[column_name][meta]

    def to_dict(self):
        return self._content

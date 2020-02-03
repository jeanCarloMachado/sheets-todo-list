

class Column:
    def __init__(self, val):
        self._val = val

    def increment_indice(self, indice):
        return chr(ord(self._val) + indice)
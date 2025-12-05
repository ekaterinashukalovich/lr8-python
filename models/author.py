class Author:
    def __init__(self, name: str, group: str):
        self.name = name
        self.group = group

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Неверно задано имя")
        self.__name = value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Неверно задана группа")
        self.__group = value

class User:
    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name

    # ---- ID ----
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: int):
        if type(value) is int and value > 0:
            self.__id = value
        else:
            raise ValueError("ID пользователя должен быть положительным целым числом")

    # ---- Имя ----
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) is str and len(value) >= 2:
            self.__name = value
        else:
            raise ValueError("Имя пользователя должно содержать больше 2 символов")


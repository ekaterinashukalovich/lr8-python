class Currency:
    def __init__(self, currency_id: str, num_code: str, char_code: str, name: str, value: float, nominal: int):
        self.currency_id = currency_id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value  
        self.nominal = nominal

    # ---- currency_id ----
    @property
    def currency_id(self):
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, value: str):
        if type(value) is str and len(value) >= 2:
            self.__currency_id = value
        else:
            raise ValueError("ID валюты должен содержать больше 2 символов")

    # ---- num_code ----
    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, value: str):
        if type(value) is str and value.isdigit():
            self.__num_code = value
        else:
            raise ValueError("Цифровой код должен состоять только из цифр")

    # ---- char_code ----
    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, value: str):
        if type(value) is str and len(value) == 3:
            self.__char_code = value
        else:
            raise ValueError("Символьный код должен состоять из 3 букв")

    # ---- name ----
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) is str and len(value) >= 2:
            self.__name = value
        else:
            raise ValueError("Название валюты должно содержать больше 2 символов")

    # ---- value ----
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, number: float):
        if (type(number) in (int, float)) and number > 0:
            self.__value = float(number)
        else:
            raise ValueError("Курс валюты должен быть положительным числом")

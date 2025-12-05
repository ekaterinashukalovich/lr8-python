from .user import User
from .currency import Currency

class UserCurrency:
    def __init__(self, user_id: int, currency_id: str):
        self.user_id = user_id
        self.currency_id = currency_id

    # ---- user_id ----
    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value: int):
        if type(value) is int and value > 0:
            self.__user_id = value
        else:
            raise ValueError("ID пользователя должен быть положительным целым числом")

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


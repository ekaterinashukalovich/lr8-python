class App:
    def __init__(self, name: str, version: str, author):
        self.name = name
        self.version = version
        self.author = author

    # ---- name ----
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if type(value) is str and len(value) >= 2:
            self.__name = value
        else:
            raise ValueError("Название приложения должно содержать больше 2 символов")

    # ---- version ----
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value: str):
        if type(value) is str and len(value) >= 1:
            self.__version = value
        else:
            raise ValueError("Версия приложения должна быть непустой строкой")

    # ---- author ----
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        from models.author import Author
        if isinstance(value, Author):
            self.__author = value
        else:
            raise ValueError("author должен быть объектом Author")

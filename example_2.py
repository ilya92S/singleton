"""Пример паттерна singleton"""


class Singleton:
    """
    Класс содержащий только один экземпляр класса
    Attr: __instanse ссылка на экземпляр класса, если его нет, принимает значение None
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        """Метод присваивает адресс только что созданного экземпляра класса"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        """Метод создает атрибут класса ,когда объект будет удален сборщиком мусора"""
        Singleton.__instance = None

    def __init__(self, name, psw):
        """Метод инициализации класса, содержит приватные атрибуты"""
        self.__name = name
        self.__psw = psw

    @property
    def name(self):
        """Геттер для получения первого приватного атрибута"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Сеттер для получения первого приватного атрибута"""
        self.__name = new_name

    @property
    def psw(self):
        """Геттер для получения второго приватного атрибута"""
        return self.__psw

    @psw.setter
    def psw(self, new_psw):
        """Сеттер для получения второго приватного атрибута"""
        self.__psw = new_psw


person = Singleton('Igor', '5555')

person2 = Singleton('Osborn', '34456')
print(id(person))
print(id(person_2))

print(person is person_2)

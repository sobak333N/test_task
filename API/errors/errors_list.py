
class NotUniqueArtikulExc(Exception):
    def __init__(self, detail: str = "Артикул не уникальный"):
        self.detail = detail


class NotValidExternalDataExc(Exception):
    def __init__(self, detail: str = "Внешние данные не валидны"):
        self.detail = detail


class ProductDoesntExitstsExc(Exception):
    def __init__(self, detail: str = "Товара с таким артикулом не существует"):
        self.detail = detail


class ServerErrorExc(Exception):
    def __init__(self, detail: str = "Ошибка на внешнем сервере"):
        self.detail = detail


class AlreadySubscribedExc(Exception):
    def __init__(self, detail: str = "Подписка на данный товар уже оформлена"):
        self.detail = detail
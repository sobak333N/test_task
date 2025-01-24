
class ProductDoesntExitstsExc(Exception):
    def __init__(self, detail: str = "Товара с таким артикулом не существует"):
        self.detail = detail


class NotValidArtikulExc(Exception):
    def __init__(self, detail: str = "Введенный артикул не валиден"):
        self.detail = detail
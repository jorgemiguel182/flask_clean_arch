from src.domain.entity.Dimensions import Dimensions


class Item:
    def __init__(self, id: int, descricao: str, preco: float, height: float = 0, width: float = 0, depth: float = 0, weight: float = 0):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.dimensions = Dimensions(height, width, depth, weight)

    def calculate_volume(self):
        return self.dimensions.calculate_volume()

    def calculate_density(self):
        return self.dimensions.calculate_density()

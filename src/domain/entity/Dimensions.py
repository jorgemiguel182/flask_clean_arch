from src.Exceptions import DimensionNegative


class Dimensions:
    height: float   # altura em centimetros
    width: float    # largura em centimetros
    depth: float    # profundidade em centimetros
    weight: float    # peso em kilogramas

    def __init__(self, height: float, width: float, depth: float, weight: float):
        if height < 0 or width < 0 or depth < 0 or weight < 0:
            raise DimensionNegative()
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight

    def calculate_volume(self) -> float:
        return (self.height/100) * (self.width/100) * (self.depth/100)

    def calculate_density(self) -> float:
        volume = self.calculate_volume()
        if volume == 0: return 0
        return self.weight / volume

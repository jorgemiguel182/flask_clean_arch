from src.domain.entity.Item import Item

MIN_FREIGHT = 10


class CalculateFreight:
    item: Item
    distance: float = 1000

    def __init__(self, item: Item):
        self.item = item

    def calculate(self, quantity: int = 1):
        volume = self.item.calculate_volume()
        density = self.item.calculate_density()
        frete = volume * self.distance * (density/100)
        if frete == 0: return 0
        return max(MIN_FREIGHT, frete) * quantity

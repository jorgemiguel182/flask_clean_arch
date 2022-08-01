MIN_FREIGHT = 10.0


class FreightCalculator:
    @staticmethod
    def calculate(distance: float, volume: float, density: float):
        freight = volume * distance * (density/100)
        if freight == 0: return 0
        return round(max(MIN_FREIGHT, freight), 2)

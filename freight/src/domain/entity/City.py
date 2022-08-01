from src.domain.entity.Coordinate import Coordinate


class City:
    coordinate: Coordinate

    def __init__(self, id_city: str, name: str, lat: float, long: float):
        self.id_city = id_city
        self.name = name
        self.long = long
        self.coordinate = Coordinate(lat, long)

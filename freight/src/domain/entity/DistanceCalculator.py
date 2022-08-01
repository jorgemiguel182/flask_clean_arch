import math
from src.domain.entity.Coordinate import Coordinate


class DistanceCalculator:
    @staticmethod
    def calculate(distance_from: Coordinate, distance_to: Coordinate) -> float:
        if distance_from.lat == distance_to.lat and distance_from.long == distance_to.long:
            return 0
        radlat1 = (math.pi * float(distance_from.lat)) / 180
        radlat2 = (math.pi * float(distance_to.lat)) / 180
        theta = distance_from.long - distance_to.long
        radtheta = (math.pi * float(theta)) / 180
        dist = math.sin(radlat1) * math.sin(radlat2) + math.cos(radlat1) * math.cos(radlat2) * math.cos(radtheta)
        if dist > 1: dist = 1
        dist = math.acos(dist)
        dist = (dist * 180) / math.pi
        dist = dist * 60 * 1.1515
        dist = dist * 1.609344 # convert miles to km
        print("dist >> ", dist)
        print("dist >> ", type(dist))
        return dist

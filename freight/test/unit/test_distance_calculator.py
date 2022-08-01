from src.domain.entity.Coordinate import Coordinate
from src.domain.entity.DistanceCalculator import DistanceCalculator


def test_calcular_distancia_entre_2_cidades():
    coordinate_from = Coordinate(-22.9129, -43.2003)
    coordinate_to = Coordinate(-27.5945, -48.5477)
    distance = DistanceCalculator.calculate(coordinate_from, coordinate_to)
    assert distance == 748.2217780081631

from dataclasses import dataclass

from src.domain.entity.DistanceCalculator import DistanceCalculator
from src.domain.entity.FreightCalculator import FreightCalculator
from src.domain.repository.CityRepository import CityRepository


@dataclass
class OrderItems:
    volume: float
    density: float
    quantity: int


@dataclass
class Input:
    cep_from: str
    cep_to: str
    order_items: [OrderItems]


@dataclass
class Output:
    total: float


class CalculateFreightUseCase:
    def __init__(self, city_repository: CityRepository):
        self.city_repository = city_repository

    def execute(self, input: Input) -> Output:
        city_from = self.city_repository.get_by_zip_code(input.cep_from)
        city_to = self.city_repository.get_by_zip_code(input.cep_to)
        distance = DistanceCalculator.calculate(city_from.coordinate, city_to.coordinate)
        total = 0
        for order_item in input.order_items:
            total += FreightCalculator.calculate(distance, order_item.volume, order_item.density) * order_item.quantity
        return Output(total)

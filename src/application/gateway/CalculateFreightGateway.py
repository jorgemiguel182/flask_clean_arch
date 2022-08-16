from abc import ABC, abstractmethod
from dataclasses import dataclass


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


class CalculateFreightGateway(ABC):
    @abstractmethod
    def calculate(self, input_dto: Input) -> Output:
        raise NotImplementedError("Subclass should be implemented.")

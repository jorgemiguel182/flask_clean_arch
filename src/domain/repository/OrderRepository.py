from abc import ABC, abstractmethod
from src.domain.entity.Order import Order
from src.domain.entity.OrderItem import OrderItem


class OrderRepository(ABC):

    @abstractmethod
    def get_by_code(self, code: str) -> Order:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def get_order_items_by_order_id(self, order_id: str) -> [OrderItem]:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def list(self) -> list[Order]:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def save(self, order: Order) -> Order:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def clean(self):
        raise NotImplementedError("Subclasses should implement this!")

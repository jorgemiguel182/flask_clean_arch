from src.domain.entity.Order import Order
from src.infra.repository.database.OrderRepositoryDatabase import OrderRepositoryDatabase


class ListOrdersUseCase:
    def __init__(self, order_repository: OrderRepositoryDatabase):
        self.order_repository = order_repository

    def execute(self) -> list[Order]:
        return self.order_repository.list()

from src.domain.entity.Order import Order
from src.domain.repository.OrderRepository import OrderRepository


class GetOrderByIdUseCase:
    def __init__(self, orderReposirory: OrderRepository):
        self.order_repository = orderReposirory

    def execute(self, code: str) -> Order:
        return self.order_repository.get_by_code(code)

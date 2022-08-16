from typing import Dict
from src.domain.entity.Order import Order
from src.domain.repository.ItemRepository import ItemRepository
from src.infra.dto import OrderPreviewDTO


class OrderPreviewUseCase:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def execute(self, input: Dict) -> float:
        validate_schema = OrderPreviewDTO.validateJson(input)
        if not validate_schema: raise Exception("Invalid input")
        order = Order(input.get("cpf"))
        for order_item in input.get("order_items"):
            item = self.item_repository.get_item_by_id(order_item.get("id_item"))
            order.add_item(item, order_item.get("quantity"))
        return order.get_total()

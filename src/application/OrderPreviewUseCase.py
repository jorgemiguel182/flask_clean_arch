from src.domain.repository.ItemRepository import ItemRepository
from src.infra.dto.OrderItemDTO import OrderItemDTO
from src.domain.entity.CalculateFreight import CalculateFreight


class OrderPreviewUseCase:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def execute(self, order_items: list[OrderItemDTO]) -> dict:
        total = 0
        for order_item in order_items:
            item = self.item_repository.get_item_by_id(order_item.id_item)
            total += CalculateFreight(item).calculate(order_item.quantidade)

        return {
            "total": total
        }
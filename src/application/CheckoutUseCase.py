from src.domain.entity.Order import Order
from src.domain.repository.ItemRepository import ItemRepository
from src.domain.repository.OrderRepository import OrderRepository
from src.infra.dto.OrderDTO import OrderDTO


class CheckoutUseCase:
    def __init__(self, itemRepository: ItemRepository, orderReposirory: OrderRepository):
        self.itemRepository = itemRepository
        self.orderRepository = orderReposirory

    def execute(self, input_dto: OrderDTO) -> dict:
        sequence = self.orderRepository.count() + 1
        order = Order(input_dto.cpf, input_dto.date, sequence)
        for order_item in input_dto.order_items:
            item = self.itemRepository.get_item_by_id(order_item.id_item)
            order.add_item(item, order_item.quantidade)
        self.orderRepository.save(order)
        total = order.get_total()
        return {
            "code": order.get_code(),
            "total": str(total)
        }
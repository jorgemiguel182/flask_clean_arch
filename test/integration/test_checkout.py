from datetime import datetime

from src.application.CheckoutUseCase import CheckoutUseCase
from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.repository.database.ItemRepositoryDatabase import ItemRepositoryDatabase
from src.infra.repository.database.OrderRepositoryDatabase import OrderRepositoryDatabase
from src.infra.dto.OrderDTO import OrderDTO
from src.infra.dto.OrderItemDTO import OrderItemDTO


def test_checkout_com_2_itens():
    connection = Psycopg2Adapter()
    itemRepository = ItemRepositoryDatabase(connection)
    orderRepository = OrderRepositoryDatabase(connection)
    checkout = CheckoutUseCase(itemRepository, orderRepository)

    orderRepository.clean()
    order_items = list()
    order_items.append(OrderItemDTO(1, 1))
    order_items.append(OrderItemDTO(2, 5))
    dto = OrderDTO(cpf="624.390.210-24", date=datetime.today(), order_items=order_items)
    output = checkout.execute(dto)
    print("test_checkout_com_2_itens output>> ", output)
    assert output.get("total") == "1080"
    assert output.get("code") == "202200000001"

from datetime import datetime

from src.application.CheckoutUseCase import CheckoutUseCase
from src.application.ListOrdersUseCase import ListOrdersUseCase
from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.dto.OrderDTO import OrderDTO
from src.infra.dto.OrderItemDTO import OrderItemDTO
from src.infra.repository.database.ItemRepositoryDatabase import ItemRepositoryDatabase
from src.infra.repository.database.OrderRepositoryDatabase import OrderRepositoryDatabase


def test_get_list_orders():
    connection = Psycopg2Adapter()
    order_repository = OrderRepositoryDatabase(connection)
    item_repository = ItemRepositoryDatabase(connection)

    # criar order no banco primeiro
    checkout = CheckoutUseCase(item_repository, order_repository)
    order_repository.clean()

    order_items = list()
    order_items.append(OrderItemDTO(1, 1))
    order_items.append(OrderItemDTO(2, 5))
    dto_1 = OrderDTO(cpf="624.390.210-24", date=datetime.today(), order_items=order_items)
    dto_2 = OrderDTO(cpf="513.521.050-47", date=datetime.today(), order_items=order_items)
    output_order_1 = checkout.execute(dto_1)
    output_order_2 = checkout.execute(dto_2)

    use_case = ListOrdersUseCase(order_repository)
    result = use_case.execute()
    assert len(result) == 2


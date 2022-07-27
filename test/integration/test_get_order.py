from datetime import datetime

from src.application.CheckoutUseCase import CheckoutUseCase
from src.application.GetOrderByIdUseCase import GetOrderByIdUseCase
from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.dto.OrderCodeDTO import OrderCodeDTO
from src.infra.dto.OrderDTO import OrderDTO
from src.infra.dto.OrderItemDTO import OrderItemDTO
from src.infra.repository.database.ItemRepositoryDatabase import ItemRepositoryDatabase
from src.infra.repository.database.OrderRepositoryDatabase import OrderRepositoryDatabase


def test_recuperar_pedido_id_use_case():
    connection = Psycopg2Adapter()
    order_repository = OrderRepositoryDatabase(connection)
    item_repository = ItemRepositoryDatabase(connection)

    # criar order no banco primeiro
    checkout = CheckoutUseCase(item_repository, order_repository)
    order_repository.clean()
    order_items = list()
    order_items.append(OrderItemDTO(1, 1))
    order_items.append(OrderItemDTO(2, 5))
    dto = OrderDTO(cpf="624.390.210-24", date=datetime.today(), order_items=order_items)
    output = checkout.execute(dto)

    order_dto = OrderCodeDTO(output.get("code"))
    use_case = GetOrderByIdUseCase(order_repository)
    order = use_case.execute(order_dto.code)
    assert order.get_code() == "202200000001"

from src.application.OrderPreviewUseCase import OrderPreviewUseCase
from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.dto.OrderItemDTO import OrderItemDTO
from src.infra.repository.database.ItemRepositoryDatabase import ItemRepositoryDatabase


def test_deve_simular_o_frete():
    connection = Psycopg2Adapter()
    item_repository = ItemRepositoryDatabase(connection)
    order_items = [
        OrderItemDTO(1, 1),
        OrderItemDTO(2, 5),
    ]
    freight = OrderPreviewUseCase(item_repository)
    value = freight.execute(order_items)
    assert value.get("total") == 60

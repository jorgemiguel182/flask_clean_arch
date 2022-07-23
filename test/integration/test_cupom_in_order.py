from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.repository.database.OrderRepositoryDatabase import OrderRepositoryDatabase
from src.domain.entity.Order import Order
from src.domain.entity.Item import Item

def testa_cupom_no_pedido():
    connection = Psycopg2Adapter()
    orderRepository = OrderRepositoryDatabase(connection)
    cupomRepository = CupomRepositoryDatabase(connection)
    cupom_use_case = ValidateCupomUseCase(CupomRepository)
    orderRepository.clean()
    order = Order("624.390.210-24")
    order.add_item(Item(1, "Twisted Metal 3", 150), 2)
    order.add_item(Item(1, "Metal Slug 2", 190), 4)
    output = cupom_use_case.execute()
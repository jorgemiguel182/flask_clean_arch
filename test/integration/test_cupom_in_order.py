from datetime import datetime
from src.application.ValidateCupomUseCase import ValidateCupomUseCase
from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.dto.CupomDTO import CupomDTO
from src.infra.repository.database.CupomRepositoryDatabase import CupomRepositoryDatabase
from src.infra.repository.database.OrderRepositoryDatabase import OrderRepositoryDatabase


def testa_cupom_no_pedido():
    connection = Psycopg2Adapter()
    orderRepository = OrderRepositoryDatabase(connection)
    cupomRepository = CupomRepositoryDatabase(connection)
    cupom_use_case = ValidateCupomUseCase(cupomRepository)
    orderRepository.clean()

    cupom_dto = CupomDTO("BRANAS10", datetime.strptime("2022-07-24T00:00:01", "%Y-%m-%dT%H:%M:%S"))
    output = cupom_use_case.execute(cupom_dto)
    assert output == True

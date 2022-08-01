import src.application.CalculateFreightUseCase as use_case
from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.repository.CityRepositoryDatabase import CityRepositoryDatabase


def test_calcular_distancia_entre_2_ceps():
    order_item = use_case.OrderItems(0.03, 100, 1)
    input = use_case.Input("22060030", "88015600", [order_item])

    connection = Psycopg2Adapter()
    city_repository = CityRepositoryDatabase(connection)
    calculate_freight = use_case.CalculateFreightUseCase(city_repository)
    output = calculate_freight.execute(input)
    assert output.total == 22.45
    connection.close()
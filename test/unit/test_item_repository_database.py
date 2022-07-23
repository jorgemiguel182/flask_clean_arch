from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.repository.database.ItemRepositoryDatabase import ItemRepositoryDatabase


def test_retorna_item_existente():
    connection = Psycopg2Adapter()
    item = ItemRepositoryDatabase(connection).get_item_by_id(1)
    assert item.descricao == "Twisted Metal 3"

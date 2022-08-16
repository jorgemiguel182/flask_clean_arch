from dependency_injector import containers, providers

from src.infra.database.Psycopg2Adapter import Psycopg2Adapter
from src.infra.repository.database.ItemRepositoryDatabase import ItemRepositoryDatabase


class Container(containers.DeclarativeContainer):
    connection = providers.Factory(Psycopg2Adapter)
    item_repository = providers.Factory(ItemRepositoryDatabase, connection=connection)
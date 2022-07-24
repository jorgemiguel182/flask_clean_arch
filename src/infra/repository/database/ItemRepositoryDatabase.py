from src.domain.entity.Item import Item
from src.domain.repository.ItemRepository import ItemRepository
from src.infra.database.Connection import Connection


class ItemRepositoryDatabase(ItemRepository):
    def __init__(self, connection: Connection):
        self.connection = connection

    def get_item_by_id(self, id: int) -> Item:
        sql = "SELECT * FROM cccat7.item WHERE id = %s"
        params = (id, )
        records = self.connection.query(sql, params, False)
        print("get_item_by_id ITEM REPOSITORY >> ", records)
        return Item(records[0][0], records[0][1], records[0][2], records[0][3], records[0][4], records[0][5], records[0][6])

    def save(self, item: Item) -> int:
        sql = "INSERT INTO cccat7.item (id, descricao, preco, height, width, depth, weight) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        params = (item.id, item.descricao, item.preco, item.dimensions.height, item.dimensions.width, item.dimensions.depth, item.dimensions.weight, )
        self.connection.query(sql, params, True)
        return item.id

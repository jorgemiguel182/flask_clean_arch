from src.domain.entity.Order import Order
from src.domain.repository.OrderRepository import OrderRepository
from src.infra.database.Connection import Connection


class OrderRepositoryDatabase(OrderRepository):
    def __init__(self, connection: Connection):
        self.connection = connection

    def save(self, order: Order) -> Order:
        sql = "INSERT INTO cccat7.order (code, cpf, freight) VALUES (%s,%s,%s) RETURNING id"
        params = (order.get_code(), order.cpf.get_value(), order.freight,)
        results = self.connection.query(sql, params)
        print("RESULTS SAVE ORDER REPOSITORY DATABASE > ", results)
        for order_item in order.order_itens:
            sql = """INSERT INTO cccat7."orderItem" (item_id, preco, quantidade, order_id) VALUES (%s,%s,%s,%s) RETURNING id"""
            params = (order_item.id_item, order_item.preco, order_item.quantidade, results[0][0])
            print("PARAMS SAVE ORDERITEM REPOSITORY >> ", params)
            self.connection.query(sql, params)
        return order

    def count(self) -> int:
        results = self.connection.query("SELECT count(*) FROM cccat7.order", (None, ))
        print("RESULT COUNT >>> ", results)
        return int(results[0][0])

    def clean(self):
        self.connection.query("DELETE FROM cccat7.\"orderItem\"", (None, ))
        self.connection.query("DELETE FROM cccat7.order", (None, ))
        return

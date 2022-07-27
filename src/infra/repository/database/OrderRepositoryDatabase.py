from src.domain.entity.Order import Order
from src.domain.entity.OrderItem import OrderItem
from src.domain.repository.OrderRepository import OrderRepository
from src.infra.database.Connection import Connection


class OrderRepositoryDatabase(OrderRepository):
    def __init__(self, connection: Connection):
        self.connection = connection

    def get_by_code(self, code: str) -> Order:
        sql_order = "SELECT * FROM cccat7.order WHERE code = %s"
        params_order = (code, )
        order_results = self.connection.query(sql_order, params_order, False)
        order = Order(order_results[0][2], order_results[0][6], order_results[0][7])
        order_items_result = self.get_order_items_by_order_id(order_results[0][0])
        order.order_itens = order_items_result
        return order

    def list(self) -> list[Order]:
        sql_order = "SELECT * FROM cccat7.order"
        params_order = ()
        order_results = self.connection.query(sql_order, params_order, False)
        result: list[Order] = []
        for order_result in order_results:
            order = Order(order_result[2], order_result[6], order_result[7])
            order_items = self.get_order_items_by_order_id(order_result[0])
            order.order_itens = order_items
            result.append(order)
        return result

    def save(self, order: Order) -> Order:
        sql = "INSERT INTO cccat7.order (code, cpf, freight, issue_date, sequence, cupom_code, cupom_percentage, total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"
        params = (order.get_code(), order.cpf.get_value(), order.freight, order.issue_date, order.sequence, order.get_cupom_code(), order.get_cupom_percentage(), order.get_total() )
        results = self.connection.query(sql, params, True)
        print("RESULTS SAVE ORDER REPOSITORY DATABASE > ", results)
        for order_item in order.order_itens:
            sql = """INSERT INTO cccat7."orderItem" (item_id, preco, quantidade, order_id) VALUES (%s,%s,%s,%s) RETURNING id"""
            params = (order_item.id_item, order_item.preco, order_item.quantidade, results[0][0])
            print("PARAMS SAVE ORDERITEM REPOSITORY >> ", params)
            self.connection.query(sql, params, True)
        return order

    def get_order_items_by_order_id(self, order_id: str) -> [OrderItem]:
        sql_ordem_item = """SELECT * FROM cccat7."orderItem" WHERE order_id = %s"""
        params_order_item = (order_id,)
        order_items_result = self.connection.query(sql_ordem_item, params_order_item, False)
        response: list[OrderItem] = []
        for order_item in order_items_result:
            response.append(OrderItem(order_item[1], order_item[2], order_item[3]))
        return response

    def count(self) -> int:
        results = self.connection.query("SELECT count(*) FROM cccat7.order", (None, ), False)
        print("RESULT COUNT >>> ", results)
        return int(results[0][0])

    def clean(self):
        self.connection.query("DELETE FROM cccat7.\"orderItem\"", (None, ), True)
        self.connection.query("DELETE FROM cccat7.order", (None, ), True)
        return

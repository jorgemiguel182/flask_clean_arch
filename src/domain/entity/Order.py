from datetime import datetime

from src.domain.entity.CPF import CPF
from src.domain.entity.CalculateFreight import CalculateFreight
from src.domain.entity.OrderCode import OrderCode
from src.domain.entity.OrderCupom import OrderCupom
from src.domain.entity.OrderItem import OrderItem
from src.domain.entity.Item import Item
from src.domain.entity.Cupom import Cupom
import src.Exceptions as exceptions


class Order:
    code: OrderCode
    cpf: CPF
    order_itens: list[OrderItem]
    cupom: OrderCupom
    freight: float
    issue_date: datetime
    sequence: int

    def __init__(self, cpf: str, date: datetime = datetime.today(), sequence: int = 1):
        self.code = OrderCode(date, sequence)
        self.cpf = CPF(cpf)
        self.order_itens = []
        self.cupom = None
        self.freight = 0
        self.issue_date = date
        self.sequence = sequence

    def get_code(self):
        return self.code.value

    def get_cupom_code(self):
        if self.cupom:
            return self.cupom.code
        return None

    def get_cupom_percentage(self):
        if self.cupom:
            return self.cupom.percentage
        return None

    def add_item(self, item: Item, quantidade: int):
        if [x for x in self.order_itens if x.id_item == item.id]: raise exceptions.ItemAlreadyInOrder()
        self.order_itens.append(OrderItem(item.id, item.preco, quantidade))
        self.freight += CalculateFreight(item).calculate()

    def add_cupom(self, cupom: Cupom):
        if cupom.is_expired(datetime.today()): return
        self.cupom = cupom.create_order_cupom()

    def get_total(self):
        total = sum([total.get_total() for total in self.order_itens])
        if self.cupom:
            total = total - self.cupom.get_discount(total)

        if self.freight:
            print("VALOR DO FRETE > ", self.freight)
            total -= self.freight
        return total

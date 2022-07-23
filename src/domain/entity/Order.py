from datetime import datetime

from src.domain.entity.CPF import CPF
from src.domain.entity.CalculateFreight import CalculateFreight
from src.domain.entity.OrderCode import OrderCode
from src.domain.entity.OrderItem import OrderItem
from src.domain.entity.Item import Item
from src.domain.entity.Cupom import Cupom
import src.Exceptions as exceptions


class Order:
    code: OrderCode
    cpf: CPF
    order_itens: list[OrderItem]
    cupoms: list[Cupom]
    freight: float

    def __init__(self, cpf: str, date: datetime = datetime.today(), sequence: int = 1):
        self.code = OrderCode(date, sequence)
        self.cpf = CPF(cpf)
        self.order_itens = []
        self.cupoms = []
        self.freight = 0

    def get_code(self):
        return self.code.value

    def add_item(self, item: Item, quantidade: int):
        if [x for x in self.order_itens if x.id_item == item.id]: raise exceptions.ItemAlreadyInOrder()
        self.order_itens.append(OrderItem(item.id, item.preco, quantidade))
        self.freight += CalculateFreight(item).calculate()

    def add_cupom(self, cupom: Cupom):
        if cupom.is_expired(datetime.today()): return
        self.cupoms.append(cupom)

    def get_total(self):
        total = sum([total.get_total() for total in self.order_itens])
        if self.cupoms:
            for cupom in self.cupoms:
                total = total - cupom.retorna_desconto_sobre_valor(total)

        if self.freight:
            print("VALOR DO FRETE > ", self.freight)
            total -= self.freight
        return total

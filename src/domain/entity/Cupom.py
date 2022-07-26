from datetime import datetime

from src.domain.entity.OrderCupom import OrderCupom


class Cupom:
    codigo: str
    porcentagem_desconto: float
    expire_date: datetime

    def __init__(self, codigo: str, porcentagem_desconto: float, expire_date: datetime):
        self.codigo = codigo
        self.porcentagem_desconto = porcentagem_desconto
        self.expire_date = expire_date

    def retorna_desconto_sobre_valor(self, valor: float) -> float:
        return (valor * self.porcentagem_desconto) / 100

    def is_expired(self, date_input: datetime):
        print("self.expire_date >> ", self.expire_date)
        print("date_input >> ", date_input)
        # return self.expire_date < date_input
        return date_input > self.expire_date

    def create_order_cupom(self) -> OrderCupom:
        return OrderCupom(self.codigo, self.porcentagem_desconto)

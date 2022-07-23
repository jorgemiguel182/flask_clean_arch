from datetime import datetime


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

    def is_expired(self, date: datetime):
        return self.expire_date < date

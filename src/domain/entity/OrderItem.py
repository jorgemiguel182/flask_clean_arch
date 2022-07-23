from src.Exceptions import OrderItemQuantityInvalid


class OrderItem:
    id_item: int
    preco: float
    quantidade: int

    def __init__(self, id_item: int, preco: float, quantidade: int):
        if quantidade < 0:
            raise OrderItemQuantityInvalid()
        self.id_item = id_item
        self.preco = preco
        self.quantidade = quantidade

    def get_total(self):
        return self.preco * self.quantidade

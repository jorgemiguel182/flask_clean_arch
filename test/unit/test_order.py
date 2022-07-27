import pytest
from datetime import datetime
import src.Exceptions as exception
from src.domain.entity.Order import Order
from src.domain.entity.Item import Item
from src.domain.entity.Cupom import Cupom


def test_pedido_cpf_numeros_iguals():
    with pytest.raises(Exception):
        Order("111.111.111-11")


def test_pedido_cpf_tamanho_invalido():
    with pytest.raises(Exception):
        Order("122.111.111-111")


def test_pedido_com_3_itens():
    order = Order("509.070.180-68")
    order.add_item(Item(1, "Twisted Metal 3", 150), 2)
    order.add_item(Item(2, "Metal Slug 2", 190), 4)
    order.add_item(Item(3, "Driver 2", 110), 1)
    assert order.get_total() == 1170


def test_pedido_com_3_itens_e_cupom_10_porcento_desconto_valido():
    order = Order("624.390.210-24")
    order.add_item(Item(7, "Twisted Metal 3", 150), 2)
    order.add_item(Item(8, "Metal Slug 2", 190), 4)
    order.add_item(Item(9, "Driver 2", 110), 1)
    cupom = Cupom("BRANAS10", 10, datetime.strptime("2023-01-01T00:00:01", "%Y-%m-%dT%H:%M:%S"))
    order.add_cupom(cupom)
    assert order.get_total() == 1053.0


def test_pedido_com_2_itens_e_cupom_expirado():
    order = Order("624.390.210-24")
    order.add_item(Item(7, "Twisted Metal 3", 150), 2)
    order.add_item(Item(8, "Metal Slug 2", 190), 4)
    cupom = Cupom("BRANAS10", 10, datetime.strptime("2020-01-01T00:00:01", "%Y-%m-%dT%H:%M:%S"))
    order.add_cupom(cupom)
    assert not order.cupom


def test_pedido_com_quantidade_de_item_negativo():
    with pytest.raises(exception.OrderItemQuantityInvalid):
        order = Order("624.390.210-24")
        order.add_item(Item(7, "Twisted Metal 3", 150), -2)


def test_pedido_com_item_duplicado():
    with pytest.raises(exception.ItemAlreadyInOrder):
        order = Order("624.390.210-24")
        order.add_item(Item(7, "Twisted Metal 3", 150), 2)
        order.add_item(Item(7, "Twisted Metal 3", 150), 1)


def test_pedido_com_calculo_frete():
    order = Order("624.390.210-24")
    order.add_item(Item(7, "Twisted Metal 3", 150, 10, 14, 14, 1.5), 1)
    order.add_item(Item(8, "Metal Slug 2", 190, 10, 14, 14, 1.5), 1)
    assert order.get_total() == 310.0


def test_pedido_com_calculo_frete_valor_minimo():
    order = Order("624.390.210-24")
    order.add_item(Item(1, "Twisted Metal 3", 150, 1, 14, 14, 0.1), 1)
    order.add_item(Item(2, "Metal Slug 2", 190, 1, 14, 14, 0.1), 1)
    order.add_item(Item(3, "Driver 2", 110, 1, 14, 14, 0.1), 1)
    assert order.get_total() == 420.0
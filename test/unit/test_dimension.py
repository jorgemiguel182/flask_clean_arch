import pytest

from src.domain.entity.Dimensions import Dimensions
import src.Exceptions as exception


def test_dimensao_valida():
    dimensao = Dimensions(1, 14, 14, 0.1)
    assert dimensao.calculate_volume() == 0.00019600000000000005
    assert dimensao.calculate_density() == 510.20408163265296


def test_dimensao_altura_negativa():
    with pytest.raises(exception.DimensionNegative):
        Dimensions(-1, 14, 14, 0.1)


def test_dimensao_largura_negativa():
    with pytest.raises(exception.DimensionNegative):
        Dimensions(1, -14, 14, 0.1)


def test_dimensao_profundidade_negativa():
    with pytest.raises(exception.DimensionNegative):
        Dimensions(1, 14, -14, 0.1)


def test_dimensao_peso_negativa():
    with pytest.raises(exception.DimensionNegative):
        Dimensions(1, 14, 14, -0.1)
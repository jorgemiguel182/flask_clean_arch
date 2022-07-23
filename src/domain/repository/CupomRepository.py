from abc import ABC, abstractmethod
from src.domain.entity.Cupom import Cupom


class CupomRepository(ABC):
    @abstractmethod
    def get_cupom_by_codigo(self, codigo: str) -> Cupom:
        raise NotImplementedError("Subclasses should implement this!")
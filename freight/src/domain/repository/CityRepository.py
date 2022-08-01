from abc import ABC, abstractmethod
from src.domain.entity.City import City


class CityRepository(ABC):

    @abstractmethod
    def get_by_zip_code(self, doce: str) -> City:
        raise NotImplementedError("Subclasses should implement this!")
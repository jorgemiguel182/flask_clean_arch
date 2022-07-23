from abc import ABC, abstractmethod
from src.domain.entity.Item import Item


class ItemRepository(ABC):
    @abstractmethod
    def get_item_by_id(self, id: int) -> Item:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def save(self, item: Item) -> str:
        raise NotImplementedError("Subclasses should implement this!")

from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def query(self, statement: str, params: tuple):
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def close(self):
        raise NotImplementedError("Subclasses should implement this!")

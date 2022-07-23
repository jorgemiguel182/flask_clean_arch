from dataclasses import dataclass


@dataclass
class OrderItemDTO:
    id_item: int
    quantidade: int

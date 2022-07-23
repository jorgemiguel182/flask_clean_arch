from dataclasses import dataclass
from datetime import datetime
from src.infra.dto import OrderItemDTO


@dataclass
class OrderDTO:
    cpf: str
    date: datetime
    order_items: list[OrderItemDTO]

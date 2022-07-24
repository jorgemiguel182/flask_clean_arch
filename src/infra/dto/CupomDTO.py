from dataclasses import dataclass
from datetime import datetime


@dataclass
class CupomDTO:
    codigo: str
    date_to_validate: datetime
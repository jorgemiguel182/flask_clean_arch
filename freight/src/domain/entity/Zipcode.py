from dataclasses import dataclass


@dataclass
class Zipcode:
    code: str
    id_city: int
    street: str
    neighborhood: str

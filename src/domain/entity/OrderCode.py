from datetime import datetime


class OrderCode:
    value: str

    def __init__(self, date: datetime, sequence: int):
        self.value = self.__generate_order_code(date, str(sequence))

    def __generate_order_code(self, date: datetime, sequence: str) -> str:
        ano = str(date.year)
        return ano + sequence.zfill(8)

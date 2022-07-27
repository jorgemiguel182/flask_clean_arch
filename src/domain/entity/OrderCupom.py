
class OrderCupom:
    def __init__(self, code: str, percentage: float):
        self.code = code
        self.percentage = percentage

    def get_discount(self, total: float):
        return (total * self.percentage)/100

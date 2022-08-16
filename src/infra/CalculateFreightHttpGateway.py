import requests
from src.application.gateway.CalculateFreightGateway import Input, Output, CalculateFreightGateway


class CalculateFreightHttpGateway(CalculateFreightGateway):
    def calculate(self, input_dto: Input) -> Output:
        response = requests.post("http://localhost:3002/calculateFreight")
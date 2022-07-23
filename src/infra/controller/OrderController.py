from flask_restx import Resource
from src.application.CheckoutUseCase import OrderDTO

api = OrderDTO.api
_order = OrderDTO.order


@api.route('/checkout')
class CheckoutOrder(Resource):
    @api.doc("Create a order checkout")
    @api.marshal_list_with(_order, envelope="data")
    def post(self):
        return [{"id": 1, "code": "asdasd123", "cpf": "123", "freight": 10}]
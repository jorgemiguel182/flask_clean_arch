import jsonschema
from jsonschema import validate


schema = {
    'type': 'object',
       'properties': {
           'cpf': {
               'type': 'string',
           },
            'order_items':{
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "properties ": {

                        "id_item": {
                            "type": "number"
                        },
                        "quantity": {
                            "type": "number"
                        }
                    },
                    "required": ["id_item", "quantity"]
                }
            }
       },
       'required': ['cpf', 'order_items']
}


def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
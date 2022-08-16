from flask import Blueprint, g, jsonify
from flask_expects_json import expects_json
from dependency_injector.wiring import inject, Provide

from src.application.OrderPreviewUseCase import OrderPreviewUseCase
from src.domain.repository.ItemRepository import ItemRepository
from src.infra.dto import OrderPreviewDTO
from src.infra.server.containers import Container

blueprint = Blueprint('order', __name__)


@blueprint.route('/orderPreview', methods=('POST',))
@expects_json(OrderPreviewDTO.schema, check_formats=True)
@inject
def checkout_order(item_repository: ItemRepository = Provide[Container.item_repository]):
    preview_order = OrderPreviewUseCase(item_repository)
    total = preview_order.execute(g.data)
    return jsonify({"total": total})

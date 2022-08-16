from flask.app import Flask
from src.infra.controller import OrderController
from src.infra.server.containers import Container
from src.infra.server.config import config_by_name
from src.infra.server.extensions import bcrypt, cache, db, migrate, cors


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    register_extensions(app)
    register_blueprints(app)
    register_dependency_injections_modules()
    return app


def register_extensions(app: Flask):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    # jwt.init_app(app)


def register_blueprints(app: Flask):
    """Register Flask blueprints."""
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(OrderController.blueprint, origins=origins)

    app.register_blueprint(OrderController.blueprint)


def register_dependency_injections_modules():
    di = Container()
    di.wire(modules=[
        OrderController
    ])
# def register_errorhandlers(app):
#     def errorhandler(error):
#         response = error.to_json()
#         response.status_code = error.status_code
#         return response
#
#     app.errorhandler(InvalidUsage)(errorhandler)
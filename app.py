import os
from src.infra.server.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

import json
import os
from pathlib import Path

from flask import Flask
from flask_migrate import Migrate

from api import api
from api.config import config_dict
from api.models import db


def create_app() -> Flask:
    config_name = os.environ.get("CONFIG", "local")

    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    config_json_path = Path(__file__).parent / "config" / "json_schemas"
    for p in config_json_path.glob("*.json"):
        with open(p) as f:
            json_name = p.stem
            schema = json.load(f)
        app.config[json_name] = schema
    db.init_app(app)
    return app


app = create_app()
# DBマイグレーションの作成
Migrate(app, db)
# blueprintをアプリケーションに登録
app.register_blueprint(api)

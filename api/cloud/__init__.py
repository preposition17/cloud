import os

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin


def create_app(test_config: dict = None) -> Flask:

    # Application instance
    app = Flask(__name__)

    # CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # SocketIO extension
    socketio = SocketIO(cors_allowed_origins="*")
    socketio.init_app(app)

    from .get_data import get_data
    app.register_blueprint(get_data)

    from .get_data import get_data_io
    app.register_blueprint(get_data_io)

    @app.after_request
    def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        return response

    return app
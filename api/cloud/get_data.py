import time

from flask import Blueprint
from blueprint_io import IOBlueprint

from flask import request
from flask import jsonify
from flask_socketio import emit
from flask_socketio import send


get_data = Blueprint("get_data", __name__, url_prefix="/send_data")
get_data_io = IOBlueprint("get_data_io", __name__)


@get_data.route("/", methods=["POST"])
def get_data_post():
    data = request.get_json()
    get_data_io.emit("new_data", data)
    return jsonify({"success": True})

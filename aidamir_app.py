import os
import time

from flask import Blueprint
from blueprint_io import IOBlueprint

from flask import request
from flask import render_template
from flask_socketio import emit


aidamir_app = Blueprint('aidamir_app', __name__, template_folder='templates')
aidamir_app_io = IOBlueprint('aidamir_app_io', __name__)


@aidamir_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("Aidar", request.data)
    return render_template("aidamir_project.html")
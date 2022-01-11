import os
import time

from flask import Blueprint
from blueprint_io import IOBlueprint

from flask import current_app
from flask import request
from flask import render_template

from flask_socketio import emit

from flask_mqtt import Mqtt

aidamir_app = Blueprint('aidamir_app', __name__, template_folder='templates')
aidamir_app_io = IOBlueprint('aidamir_app_io', __name__)



@aidamir_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("Aidar", request.data)
    return render_template("aidamir_project.html")


class Mqqt_(Mqtt):
    def __init__(self, broker_url, broker_port, username, password, keepalive=5, tls_enabled=False):
        super().__init__()
        self.username = username
        self.password = password
        self.broker_url = broker_url
        self.broker_port = broker_port
        self.tls_enabled = tls_enabled
        self.keepalive = keepalive

    def init(self) -> None:
        if self.last_will_topic is not None:
            self.client.will_set(
                self.last_will_topic,
                self.last_will_message,
                self.last_will_qos,
                self.last_will_retain,
            )
        self._connect()


mqtt = Mqqt_("broker.hivemq.com", 1883, "aidar", "Q!@We34r")
mqtt.init()
mqtt.subscribe('test/mytopic')


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('test/mytopic')


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global data_
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    aidamir_app_io.emit("new_data", data["payload"])


@aidamir_app_io.on('message')
def test_io(data):
    print(data)










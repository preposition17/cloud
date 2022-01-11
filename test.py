import time
import os

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import current_app

from flask_socketio import SocketIO
from flask_socketio import emit

from flask_mqtt import Mqtt


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
app.config['MQTT_USERNAME'] = 'aidar'  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = 'Q!@We34r'  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 5  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes

socketio = SocketIO(app)


from ilnaz_app import ilnaz_app
from ilnaz_app import ilnaz_app_io
app.register_blueprint(ilnaz_app, url_prefix='/ilnaz-project')
app.register_blueprint(ilnaz_app_io, url_prefix='/ilnaz-project')


from aidamir_app import aidamir_app
from aidamir_app import aidamir_app_io
app.register_blueprint(aidamir_app, url_prefix='/aidar&damir-project')
app.register_blueprint(aidamir_app_io, url_prefix='/aidar&damir-project')


@app.route("/")
def hello_world():
    print("data: ", request.json)
    return "This page in developing"












if __name__ == '__main__':
    #app.run(debug=True, host="0.0.0.0", port=80)
    socketio.run(app, debug=True, host="0.0.0.0", port=80)
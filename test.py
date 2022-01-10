import time
import os

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

from flask_socketio import SocketIO
from flask_socketio import emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
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
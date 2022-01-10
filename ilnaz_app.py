import os
import time

from flask import Blueprint
from blueprint_io import IOBlueprint

from flask import request
from flask import render_template
from flask_socketio import emit

ilnaz_app = Blueprint('ilnaz_app', __name__, template_folder='templates')
ilnaz_app_io = IOBlueprint('ilnaz_app_io', __name__)


def nearest(lst, target):
    return min(lst, key=lambda x: abs(x - target))


@ilnaz_app.route("/", methods=["GET", "POST"])
def ilnaz():
    if request.method == "POST":
        with open(f"ilnaz_data/{int(time.time())}", "w") as file:
            file.write(f"t{request.json['t']}\n"
                       f"h{request.json['h']}\n"
                       f"b{request.json['b']}\n")
        return "index"
    elif request.method == "GET":

        return render_template("ilnaz_index.html")


@ilnaz_app_io.on('message')
def handle_message(data):
    filenames = os.listdir("ilnaz_data")
    filenames = [int(i) for i in filenames]
    now = int(time.time())
    last_times = [nearest(filenames, i) for i in range(now - 3600, now, 60)]
    last_data = list()
    for filename in last_times:
        with open(f"ilnaz_data/{filename}", "r") as file:
            filedata = file.readlines()
            temp = filedata[0][1:6]
            hum = filedata[1][1:6]
            last_data.append({
                "temp": temp,
                "hum": hum,
                "time": filename
            })
    emit('last_data', last_data)
    while True:
        filenames = os.listdir("ilnaz_data")
        filenames = [int(i) for i in filenames]

        first_filename = filenames[0]
        last_filename = filenames[-1]
        if time.time() - first_filename > 86400:
            try:
                os.remove(os.path.join("ilnaz_data", str(first_filename)))
            except Exception as ex:
                print("Deleting error, ", ex)

        if time.time() - last_filename > 1:
            with open(f"ilnaz_data/{last_filename}", "r") as file:
                filedata = file.readlines()
                temp = filedata[0][1:6]
                hum = filedata[1][1:6]
                btn = filedata[2][1:6]

                emit('new_data', {
                    "temp": float(temp),
                    "hum": float(hum),
                    "btn": float(btn),
                    "time": last_filename
                })
                time.sleep(1)
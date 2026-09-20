from flask import Flask, render_template, jsonify
from monitor import HealthMonitor
import threading
import time

app = Flask(__name__)
monitor = HealthMonitor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/vitals")
def vitals():
    return jsonify(monitor.get_latest())


@app.route("/api/history")
def history():
    return jsonify(monitor.get_history())


def background_reader():
    while True:
        monitor.read_sensors()
        time.sleep(2)


if __name__ == "__main__":
    threading.Thread(target=background_reader, daemon=True).start()
    app.run(debug=True, port=5000)
from flask import Flask, render_template
from flask_socketio import SocketIO
from config import current_config
import os
from flask import render_template


def create_app():
    app = Flask(__name__)
    app_config = current_config(os.getenv("ENVIRONMENT", "DEVELOPMENT"))()
    app.config.from_object(app_config)

    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html", SOCKET_URL="/")

    return app


def register_socket(app):
    # for gevent workers socket common storage as redis
    socketio = SocketIO(app, **{"message_queue": str(app.config["REDIS_CONN"])})

    @socketio.on("ping")
    def pong():
        print("ping pong")
        emit("pong", pong)

    return socketio

from flask import Flask
from config import Config
from flask_socketio import SocketIO

from .common.lang_model import LangModel

socketio = SocketIO()

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
wsgi_app = app.wsgi_app

socketio.init_app(app)

lang_model = LangModel()

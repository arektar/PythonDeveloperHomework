from flask import Blueprint, request
from app.backend_requests.backend_requests import BackendRequest
from .controllers.chat import Chat
from .controllers.login import ChatLogin
from .controllers.logout import ChatLogout

chat = Blueprint('chat', __name__, template_folder='templates', static_folder='static')


@chat.route('/')
def index():
    return BackendRequest.call(Chat, request)


@chat.route('/login', methods=["GET", "POST"])
def login():
    return BackendRequest.call(ChatLogin, request)


@chat.route('/logout', methods=["GET", "POST"])
def logout():
    return BackendRequest.call(ChatLogout, request)

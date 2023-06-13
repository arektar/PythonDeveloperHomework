from app import app
from .chat import chat

app.register_blueprint(chat)

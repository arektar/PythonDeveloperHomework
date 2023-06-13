from app import app, socketio
from config import Config
from app import routes
from app import backend_requests



if __name__ == '__main__':
    socketio.run(app, host=Config.HOST, port=Config.PORT, debug=True)

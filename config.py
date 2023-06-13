import os


class Config(object):
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

    if not SECRET_KEY:
        SECRET_KEY = '1'
        print(f'FLASK_SECRET_KEY not found and substituted with {SECRET_KEY} this will work only for local tests')

    HOST = os.environ.get('FLASK_HOST') or '0.0.0.0'
    PORT = os.environ.get('FLASK_PORT') or 5000
    if PORT is str:
        PORT = int(PORT)

    ERRORS_RISING = os.environ.get('ERRORS_RISING') or False

    DATABASE_URI = os.environ.get('DATABASE_URI') or "mongodb://localhost:27017/"

    LANGMOD_SERVICE_URL = os.environ.get('LANGMOD_SERVICE_URL') or "http://l3m.site:9000"
    LANGMOD_SERVICE_TOKEN = os.environ.get('LANGMOD_SERVICE_TOKEN') or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhX2thc3lraW4iLCJzY29wZXMiOlsicWEiLCJrbm93bGVkZ2UiXX0.5_Hnu4Y0JNzYD9nDBP4pqDMaoR-cl4HeZe9R9sYsUMc"

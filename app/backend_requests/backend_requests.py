import json
from abc import ABC, abstractmethod
from datetime import datetime

from flask import jsonify, session, flash

from config import Config


class BackendRequest(ABC):
    """ Abstract class for requests data parsing and errors handling."""
    def __init__(self, req_content, logging_enabled=False):
        self.req_content = req_content
        self.logging_enabled = logging_enabled

    @abstractmethod
    def process(self):
        pass

    @staticmethod
    def _parse_param(params, title, param_type, optional=False):
        param = params.get(title)
        if param is None:
            if optional:
                return None
            else:
                raise Exception(f'{title} param not found')
        else:
            try:
                return param_type(param)
            except Exception as exc:
                if optional:
                    return None
                else:
                    raise Exception(f'Failed to parse {title} param')

    @staticmethod
    def call(requestType, request):
        try:
            if request.is_json:
                request_json = json.loads(request.data) if request.content_length else {}
                req = requestType(request_json)
            elif request.form:
                form = request.form
                req = requestType(form)
            else:
                req = requestType({})

        except Exception as exc:
            if Config.ERRORS_RISING:
                raise exc
            flash(f"Params parse internal error: {exc}")
            return jsonify({'error': str(exc)}), 400


        try:
            result = req.process()
            return result
        except Exception as exc:
            if Config.ERRORS_RISING:
                raise exc
            flash(f"Process internal error: {exc}")
            return jsonify({'error': str(exc)}), 512

    @staticmethod
    def isLogged():
        return True if session.get('user') else False

    @staticmethod
    def login_user(user):
        session['user'] = user

    @staticmethod
    def logout_user():
        session.pop('user', None)

    def log(self, text):
        if self.logging_enabled:
            self._log(text)

    def _log(self, text):
        print(type(self).__name__, ': ', text, sep='')

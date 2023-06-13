from flask import redirect, url_for
from app.backend_requests.backend_requests import BackendRequest


class ChatLogout(BackendRequest):
    def __init__(self, req_content: dict):
        super().__init__(req_content)

    def process(self):
        if not self.isLogged():
            return redirect(url_for('.login'))

        self.logout_user()

        return redirect(url_for('.login'))

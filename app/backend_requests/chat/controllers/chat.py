from app.backend_requests.backend_requests import BackendRequest
from flask import redirect, url_for, render_template


class Chat(BackendRequest):
    def __init__(self, req_content: dict):
        super().__init__(req_content)

    def process(self):
        if not self.isLogged():
            return redirect(url_for('.login'))

        return render_template('./chat.html')

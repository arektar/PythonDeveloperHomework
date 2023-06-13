from flask import redirect, url_for, render_template, flash
from app.backend_requests.chat.models.user import User
from app.backend_requests.backend_requests import BackendRequest


class ChatLogin(BackendRequest):
    def __init__(self, req_content: dict):
        super().__init__(req_content)
        self.username = self._parse_param(req_content, 'user', str, optional=True)

    def process(self):
        if self.isLogged():
            return redirect(url_for('.index'))

        if self.username:
            user = User.from_name(self.username)
            self.login_user(user.full_doc)
            return redirect(url_for('.index'))

        return render_template('./login.html', title='Чат')

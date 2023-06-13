import pytest
from app.backend_requests.chat.models.user import User
from app.backend_requests.chat.models.chat import Chat



def test_chat_full():
    user = User.from_name('test')

    chat = Chat.from_user_id(user.user_id)

    assert type(chat) is Chat

    chat2 = Chat.get_by_id(chat.chat_id)

    assert type(chat2) is Chat
    assert chat.chat_id == chat2.chat_id
    assert chat.user.user_id == chat2.user.user_id

    chat_dict = chat.full_doc

    assert type(chat_dict) is dict
    assert chat_dict["_id"] == str(chat.chat_id)
    assert chat_dict["user_id"] == str(chat.user.user_id)

    chat3 = Chat.from_dict(chat_dict)

    assert type(chat3) is Chat
    assert chat.chat_id == chat3.chat_id
    assert chat.user.user_id == chat3.user.user_id





if __name__ == '__main__':
    test_chat_full()

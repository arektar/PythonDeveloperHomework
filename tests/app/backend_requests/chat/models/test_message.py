import pytest
from app.backend_requests.chat.models.user import User
from app.backend_requests.chat.models.chat import Chat
from app.backend_requests.chat.models.message import Message

def test_message_full():
    user = User.from_name('test')
    chat = Chat.from_user_id(user.user_id)
    message = Message.new(user.user_id,'test','test')

    assert type(message) is Message

    message2 = Message.get_by_id(message.mess_id)

    assert type(message2) is Message
    assert message2.mess_id == message2.mess_id
    assert message.chat.chat_id == message2.chat.chat_id

    mess_dict = message.full_doc

    assert type(mess_dict) is dict
    assert mess_dict["_id"] == str(message.mess_id)
    assert mess_dict["chat_id"] == str(message.chat.chat_id)

    message3 = Message.from_dict(mess_dict)

    assert type(message3) is Message
    assert message.mess_id == message3.mess_id
    assert message.chat.chat_id == message3.chat.chat_id







if __name__ == '__main__':
    test_message_full()

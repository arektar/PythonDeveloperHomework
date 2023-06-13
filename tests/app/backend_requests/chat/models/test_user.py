import pytest
from app.backend_requests.chat.models.user import User


def test_user_full():
    user = User.from_name('test')

    assert type(user) is User

    user2 = User.get_by_id(user.user_id)

    assert type(user2) is User
    assert user.user_id == user2.user_id
    assert user.name == user2.name

    user_dict = user.full_doc

    assert type(user_dict) is dict
    assert user_dict["_id"] == str(user.user_id)
    assert user_dict["name"] == user.name

    user3 = User.from_dict(user_dict)

    assert type(user3) is User
    assert user.user_id == user3.user_id
    assert user.name == user3.name






if __name__ == '__main__':
    test_user_full()
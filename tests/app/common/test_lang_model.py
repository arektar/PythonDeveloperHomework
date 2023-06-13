import pytest
from config import Config
from app.common.lang_model import LangModel


@pytest.fixture()
def resource_setup(request):
    return LangModel()


def test_get_url(resource_setup):
    model = resource_setup

    url = model.get_url("test")

    assert type(url) is str
    assert "test" in url
    assert Config.LANGMOD_SERVICE_URL in url
    assert Config.LANGMOD_SERVICE_TOKEN in url


def test_chat(resource_setup):
    model = resource_setup

    messeges = [
        {"agent": "robot", "message": "я страшно умная машина"},
        {"agent": "1", "message": "что ты умеешь?"}
    ]

    answer = model.chat(messeges)

    assert type(answer) == str
    assert len(answer) > 0


if __name__ == '__main__':
    model = resource_setup
    test_get_url(model)
    test_chat(model)

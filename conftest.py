import pytest

from api.user_api import UserAPI
from common.token_manager import TokenManager


@pytest.fixture(scope="session", autouse=True)
def login():

    api = UserAPI()

    res = api.login(
        "admin",
        "123456"
    )

    token = res.json()["token"]

    TokenManager.set_token(token)

    yield
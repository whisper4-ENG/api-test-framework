import allure
import pytest

from api.user_api import UserAPI
from common.token_manager import TokenManager
from utils.yaml_util import YamlUtil
from utils.assert_util import AssertUtil

data = YamlUtil.read_yaml(
    "data/login.yaml"
)

@allure.feature("用户模块")
class TestUser:

    @classmethod
    def setup_class(cls):

        cls.api = UserAPI()

        cls.token = None

    @pytest.mark.parametrize(
        "case",
        data.values()
    )
    def test_login(self, case):
        res = self.api.login(
            case["username"],
            case["password"]
        )

        body = res.json()

        assert body["code"] == case["expect_code"]

        if body["code"] == 200:
            TokenManager.set_token(
                body["token"]
            )

    @allure.title("获取用户信息")
    def test_user_info(self):

        token = TokenManager.get_token()

        res = self.api.get_user_info(token)

        body = res.json()

        AssertUtil.assert_code(
            body["code"],
            200
        )

        assert body["data"]["username"] == "admin"
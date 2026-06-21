import allure

from api.order_api import OrderAPI
from common.token_manager import TokenManager


@allure.feature("订单模块")
class TestOrder:

    @classmethod
    def setup_class(cls):

        cls.api = OrderAPI()

    def test_create_order(self):

        token = TokenManager.get_token()

        res = self.api.create_order(
            token,
            1,
            2
        )

        body = res.json()

        assert body["code"] == 200

        TestOrder.order_id = body["data"]["order_id"]

    def test_query_order(self):

        token = TokenManager.get_token()

        res = self.api.query_order(
            token,
            TestOrder.order_id
        )

        body = res.json()

        assert body["code"] == 200

    def test_invalid_token(self):

        res = self.api.query_order(
            "abc",
            TestOrder.order_id
        )

        body = res.json()

        assert body["code"] == 403

    def test_query_not_exist_order(self):

        token = TokenManager.get_token()

        res = self.api.query_order(
            token,
            99999
        )

        body = res.json()

        assert body["code"] == 404

    def test_create_order_quantity_zero(self):

        token = TokenManager.get_token()

        res = self.api.create_order(
            token,
            1,
            0
        )

        body = res.json()

        assert body["code"] == 400
from api.order_api import OrderAPI
from common.token_manager import TokenManager


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

        res = self.api.query_order(
            TestOrder.order_id
        )

        body = res.json()

        assert body["code"] == 200

        assert body["data"]["product_id"] == 1
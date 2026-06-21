import allure

from api.product_api import ProductAPI


@allure.feature("商品模块")
class TestProduct:

    @classmethod
    def setup_class(cls):

        cls.api = ProductAPI()

    def test_product_list(self):

        res = self.api.get_product_list()

        body = res.json()

        assert body["code"] == 200

    def test_product_detail(self):

        res = self.api.get_product_detail(
            1
        )

        body = res.json()

        assert body["code"] == 200

        assert body["data"]["name"] == "iPhone 16"

    def test_product_not_exist(self):

        res = self.api.get_product_detail(
            999
        )

        body = res.json()

        assert body["code"] == 404
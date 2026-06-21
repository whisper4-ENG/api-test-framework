from api.product_api import ProductAPI


class TestProduct:

    @classmethod
    def setup_class(cls):

        cls.api = ProductAPI()

    def test_product_list(self):

        res = self.api.get_product_list()

        body = res.json()

        assert body["code"] == 200

        assert len(
            body["data"]
        ) > 0
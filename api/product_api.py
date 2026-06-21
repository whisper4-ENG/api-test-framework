from api.base_api import BaseAPI


class ProductAPI(BaseAPI):

    def get_product_list(self):

        return self.send(
            "GET",
            "/products"
        )
from api.base_api import BaseAPI


class ProductAPI(BaseAPI):

    def get_product_list(self):
        return self.send("GET","/products")

    def get_product_detail(self,product_id):
        return self.send("GET",f"/product/{product_id}")
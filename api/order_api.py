from api.base_api import BaseAPI


class OrderAPI(BaseAPI):

    def create_order(
            self,
            token,
            product_id,
            quantity
    ):

        return self.send(
            "POST",
            "/order/create",
            headers={
                "Authorization": token
            },
            json={
                "product_id": product_id,
                "quantity": quantity
            }
        )

    def query_order(
            self,
            token,
            order_id
    ):

        return self.send(
            "GET",
            f"/order/detail/{order_id}",
            headers={
                "Authorization": token
            }
        )
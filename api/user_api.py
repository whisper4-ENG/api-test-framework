from api.base_api import BaseAPI


class UserAPI(BaseAPI):

    def login(self, username, password):

        return self.send(
            "POST",
            "/login",
            json={
                "username": username,
                "password": password
            }
        )

    def get_user_info(self, token):

        return self.send(
            "GET",
            "/user/info",
            headers={
                "Authorization": token
            }
        )
from common.base_api import BaseApi


class User(BaseApi):
    """

    """
    def login_user(self, username, password, rememberMe):
        p_data = {"ip": self.ip, "username": username, "password": password, "remeberMe": rememberMe}
        res = self.send_api_data("data/gateway_data/user_controller.yml", p_data, "user_login")
        return  res
import os

import pytest

from api.gateway_api.authenticate import User


class Testlogin():
    """

    """

    user = User()
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    # 获取data的路径，但这样写有点蠢，因为template没有对路径进行好的优化
    data_path = os.path.join(BASE_PATH, "data/gateway_data/user_data.yml")
    # 参数化的数据
    sign_data = user.load_yaml(data_path)
    print(sign_data)

    @pytest.mark.parametrize(" username, password, rememberMe, code, msg", sign_data["user_data"])
    def test_login(self, username, password, rememberMe, code, msg):
        res = self.user.login_user(username, password, rememberMe)
        print(res)


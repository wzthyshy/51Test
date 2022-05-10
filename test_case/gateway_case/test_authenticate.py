import os

import pytest
import allure

from api.gateway_api.authenticate import User
from common import get_log


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("usercontroller模块")
class Testlogin():
    """

    """

    user = User()
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    # 获取data的路径，但这样写有点蠢，因为template没有对路径进行好的优化
    data_path = os.path.join(BASE_PATH, "data/gateway_data/user_data.yml")
    # 参数化的数据
    sign_data = user.load_yaml(data_path)
    #
    # def __init__(self):
    #     self.token = None

    @allure.story("用例--用户登录")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @pytest.mark.parametrize(" username, password, rememberMe, code, msg", sign_data["user_data"])
    def test_login(self, username, password, rememberMe, code, msg):
        res = self.user.login_user(username, password, rememberMe)
        self.token = res.get('data')['token_id']
        print(res.get('code'))
        get_log.log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(code, res.get('code')))
        assert res.get('code') == code
        get_log.log.info("msg ==>> 期望结果：{}， 实际结果：【 {} 】".format(msg, res.get('msg')))
        assert res.get('msg') == msg

    @allure.story("用例--刷新token")
    @pytest.mark.parametrize("token, code", sign_data["refresh_data"])
    def test_refresh_token(self, token, code):
        res = self.user.refresh_token(token)
        print(res)
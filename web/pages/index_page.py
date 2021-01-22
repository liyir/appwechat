#对首页进行建模
from web.pages.login_page import LoginPage
from web.pages.register_page import RegisterPage

#一.编写页面所具有的功能
class IndexPage:
    def goto_login(self):
        """跳转到登录页面

        :return:
        """
        return LoginPage()

    def goto_register(self):
        """跳转到注册页面

        :return:
         """
        return RegisterPage()
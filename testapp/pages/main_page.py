# 首页PO
from appium.webdriver.common.mobileby import MobileBy

from testapp.pages.address_list_page import AddresslistPage
from testapp.pages.base_page import BasePage


class MainPage(BasePage):

    def goto_address_list(self):
        """
        进入通讯录页面
        :return:
        """
        # todo 点击通讯录按钮

        self.find_and_click(MobileBy.XPATH,'//*[@text="通讯录" and @resource-id="com.tencent.wework:id/elq"]')
        return AddresslistPage(self.driver)
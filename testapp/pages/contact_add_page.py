# 成员信息录入页面
from appium.webdriver.common.mobileby import MobileBy

from testapp.pages.base_page import BasePage


class ContactPage(BasePage):
    def add_contact(self):
        """
        添加成员信息操作
        :return:
        """
        # todo 姓名、性别、手机号填写

        # 输入框定位元素方法（相对定位）：找姓名，再找姓名的父元素，再从其中去定位“必填” ..代表父元素
        self.find_and_send_keys(MobileBy.XPATH,
                                 '//*[contains(@text,"姓名")]/..//*[@text="必填"]',"ha5")
        self.find_and_click(MobileBy.XPATH,
                                 '//*[contains(@text,"性别")]/..//*[@text="男"]')

        self.wait_for(MobileBy.XPATH,"//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='男']")
        self.find_and_send_keys(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//*[@text='手机号']","11122223344")
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        return True



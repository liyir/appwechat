# 添加成员页面
from appium.webdriver.common.mobileby import MobileBy

from testapp.pages.base_page import BasePage
from testapp.pages.contact_add_page import ContactPage


class MemberInviteMenuPage(BasePage):
    def add_member_manual(self):
        """
        进入到信息录入页面
        :return: 
        """
        # todo 点击手动输入添加按钮

        self.find_and_click(MobileBy.XPATH,'//*[@text="手动输入添加"]')
        return ContactPage(self.driver)



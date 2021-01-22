# 通讯录页面
from appium.webdriver.common.mobileby import MobileBy

from testapp.pages.base_page import BasePage
from testapp.pages.member_invite_menu_page import MemberInviteMenuPage


class AddresslistPage(BasePage):
    def goto_add_member(self):
        """
        进入到添加成员页面
        :return: 
        """
        # todo 点击添加成员按钮

        # self.scroll_find_click("添加成员")
        self.swipe_find_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return MemberInviteMenuPage(self.driver)
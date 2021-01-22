from selenium.webdriver.common.by import By

from web.pages.add_member_page import AddMemberPage
from web.pages.base_page import BasePage
from web.pages.contact_page import ContactPage


class MainPage(BasePage):
    # "_"私有变量
    _location_goto_member = (By.CSS_SELECTOR,".ww_indexImg_AddMember")
    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        # ”*“解元祖操作，把元祖内的元素拆分作为不同d的参数传入
        self.find(self._location_goto_member).click()

        return AddMemberPage(self.driver)

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def back_main(self):
        '''
        回到首页
        :return:
        '''
        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()


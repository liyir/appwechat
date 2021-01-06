from selenium.webdriver.common.by import By

from pages.add_member_page import AddMemberPage
from pages.base_page import BasePage
from pages.contact_page import ContactPage


class MainPage(BasePage):
    _lacation_goto_add_member=(By.CSS_SELECTOR, ".ww_indexImg_AddMember") #"_"使元素变为私有的，不暴露页面元素
    _location_goto_contact=(By.ID,"menu_contacts")
    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        self.find(*self._lacation_goto_add_member).click()#”*“解元组操作，把元组内的元素拆分作为不同的参数传入
        return AddMemberPage(self.driver)

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(self.goto_add_member()).click()
        return ContactPage(self.driver)

    def back_main(self):
        self.find(By.ID,"menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()


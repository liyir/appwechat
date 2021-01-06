from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.contact_page import ContactPage


# AddMemberPage类继承BasePage类，可以使用driver的实例变量
class AddMemberPage(BasePage):
    _lacation_username = (By.ID, "username")
    _lacation_acctid = (By.ID, "memberAdd_acctid")
    _location_Add_phone = (By.ID, "memberAdd_phone")
    _lacation_save=(By.CSS_SELECTOR, ".js_btn_save")

    def add_member(self):
        """
        添加成员操作
        :return:
        """
        self.find(*self._lacation_username).send_keys("哈2")
        self.find(*self._lacation_acctid).send_keys("ha2")
        self.find(*self._location_Add_phone).send_keys("18700012113")
        self.find(self._lacation_save).click()
        return ContactPage(self.driver)

    #同样的行为不同的结果可以建模为不同的方法
    def add_memeber_fail(self,acctid,phone):
        """
        添加成员失败操作
        :return:
        """
        self.find(*self._lacation_username).send_keys("哈2")
        self.find(*self._lacation_acctid).send_keys(acctid)
        self.find(*self._location_Add_phone).send_keys(phone)
        self.find(self._lacation_save).click()
        # error_message = self.find(By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # phone_error_message = self.find(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # error_list = [error_message,phone_error_message]
        res = self.finds(By.CSS_SELECTOR,".ww_inputWithTips_tips")
        print(res)
        error_list = [i.text for i in res]
        print(error_list)
        return error_list




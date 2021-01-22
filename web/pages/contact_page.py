from selenium.webdriver.common.by import By

from web.pages.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list=(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member=(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    def goto_add_member(self):
        from web.pages.add_member_page import AddMemberPage #规避掉循环导入的问题
        """
        跳转到添加成员页面

        :return:
        """
        # 添加显示等待，保证按钮可以点击（可进行底层封装）
        # WebDriverWait(self.driver,9).until(
        #     expected_conditions.element_to_be_clickable(self._location_goto_add_member))
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMemberPage(self.driver)

    def get_member_list(self):
        """
        获取成员列表，用来做断言
        :return:
        """
        self.wait_click(self._location_member_list)
        member_list=self.finds(*self._location_member_list)
        member_list_res = [i.text for i in member_list]
        # member_list2 = []
        # for i in member_list:
        #     member_list2.append(i.text)
        # print(member_list)
        return member_list_res

    def goto_add_department(self):
        from web.pages.add_department_page import AddDepartmentPage
        """
        弹出添加部门弹窗
        :return:
        """
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR,".js_create_party").click()
        return AddDepartmentPage(self.driver)

    def get_department_list(self):

        '''
        获取部门列表
        :return:
        '''
        self.wait_click()
        department_list = self.finds()
        return department_list
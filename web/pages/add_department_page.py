from selenium.webdriver.common.by import By
from web.pages.base_page import BasePage
from web.pages.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    def add_department(self):
        """
        添加部门操作
        :return:
        """
        self.find(By.NAME, "name").send_keys("部门4")
        # 点击所属部门，选择列表
        self.find(By.CSS_SELECTOR,".js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688851294547208_anchor']").click()
        self.find(By.CSS_SELECTOR,'[id=__dialog__MNDialog__] div>div>a:nth-child(1)').click()

        return ContactPage(self.driver)
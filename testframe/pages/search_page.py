import yaml
from appium.webdriver.common.mobileby import MobileBy

from testframe.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        """
        搜索操作
        :return:
        """
        # self.find_and_send_keys(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']","贵州茅台")

        # with open("../pages/search_page.yaml",encoding='utf-8') as f:
        #     data=yaml.load(f)
        # # step: find,action
        # for step in data:
        #     xpath_expr = step.get("find")
        #     action = step.get("action")
        #     if action == "find_and_click":
        #         self.find_and_click(MobileBy.XPATH,xpath_expr)
        #     elif action=="find_and_send_keys":
        #         content = step.get("content")
        #         self.find_and_send_keys(MobileBy.XPATH,xpath_expr,content)

        self.load("../pages/search_page.yaml")
        return True

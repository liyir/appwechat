import yaml
from appium.webdriver.common.mobileby import MobileBy

from testframe.base_page import BasePage
from testframe.pages.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        """
        进入搜索页面
        :return:
        """
        # self.find_and_click(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']")

        # with open("../pages/market_page.yaml",encoding='utf-8') as f:
        #     data=yaml.load(f)
        # # step: find,action
        # for step in data:
        #     xpath_expr = step.get("find")
        #     action = step.get("action")
        #     if action == "find_and_click":
        #         self.find_and_click(MobileBy.XPATH,xpath_expr)

        self.load("../pages/market_page.yaml")
        return SearchPage(self.driver)



import yaml
from appium.webdriver.common.mobileby import MobileBy

from testframe.base_page import BasePage
from testframe.pages.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        """
        进入详情页面
        :return:
        """
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")

        # todo:为什么会出现乱码
        # with open("../pages/main_page.yaml",encoding='utf-8') as f:
        #     data=yaml.load(f)
        # # step: find,action
        # for step in data:
        #     xpath_expr = step.get("find")
        #     action = step.get("action")
        #     if action == "find_and_click":
        #         self.find_and_click(MobileBy.XPATH,xpath_expr)

        # todo 为什么路径要用../pages/main_page.yaml  而不是./pages/main_page.yaml
        # 不在同一个执行目录里，所以要用../回到执行目录的上一级
        self.load("../pages/main_page.yaml")
        return MarketPage(self.driver)

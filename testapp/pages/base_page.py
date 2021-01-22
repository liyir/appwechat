# 通用操作（与driver有关），所有的子类都可以继承
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 实现driver的传递
    def __init__(self, driver: WebDriver = None):# 冒号代表注解
        self.driver = driver

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    # 查找和点击操作
    def find_and_click(self,by,locator):
        self.find(by,locator).click()

    # 滑动查找
    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                                        ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                             'scrollable(true).instance(0)).'
                                                             'scrollIntoView(new UiSelector().'
                                                             f'text("{text}").instance(0));')

    def swipe_find(self,by,locator):
        self.driver.implicitly_wait(1)
        # 找到页面所有元素
        eles = self.driver.find_elements(by,locator)
        # 不停滑动，直到找到需要的元素为止
        while len(eles) == 0:  # 数组eles长度为0，说明该数组里没有元素
            #滑动
            self.driver.swipe(0,600,0,400)
            eles = self.driver.find_elements(by,locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    def swipe_find_click(self,by,locator):
        self.swipe_find(by,locator).click()

    # 滑动查找并点击操作
    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def find_and_send_keys(self, by, locator, text):
        self.find(by,locator).send_keys(text)

    def wait_for(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by,locator)
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result










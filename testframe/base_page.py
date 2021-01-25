# 通用操作（与driver有关，与业务无关），所有的子类都可以继承
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

# 封装黑名单类 操作单元黑名单类是可以追踪的，与黑名单相关的
from testframe.black_handle import black_wrapper


class Black:
    def __init__(self):
        pass

class BasePage:
    FIND = 'find'
    ACTION = 'action'
    FIND_AND_CLICK = 'find_and_click'
    SEND = 'find_and_send_keys'
    CONTENT = 'content'

    # 实现driver的传递
    def __init__(self, driver: WebDriver = None):# 冒号代表注解
        self.driver = driver
        # 参考:封装黑名单时，声明一个黑名单类
        self.black_list = [(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")]  #black_list指黑名单列表

    # 设计模式：代理模式，装饰器模式
    # 装饰器
    @black_wrapper
    def find(self,by,locator):  # find方法被传给装饰器
        # self.driver.save_screenshot("tmp.png")
        return self.driver.find_element(by, locator)


    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)

    # 查找和点击操作
    def find_and_click(self,by,locator):
        """
        find 出现弹窗，去除弹窗；再click
        方便做黑名单的处理
        :param by:
        :param locator:
        :return:
        """
        self.find(by,locator).click()
        self.driver.start_recording_screen()

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

    # todo basepage无限膨胀问题
    def load(self, yaml_path):
        with open(yaml_path, encoding='utf-8') as f:
            data = yaml.load(f)
        # step: find,action,content
        for step in data:
            # todo：关键字可变问题  解决方法：把关键字设置为常量或者类变量
            xpath_expr = step.get(self.FIND)
            action = step.get(self.ACTION)
            # todo：函数调用
            if action == self.FIND_AND_CLICK:
                self.find_and_click(MobileBy.XPATH, xpath_expr)
            elif action == self.SEND:
                content = step.get(self.CONTENT)
                self.find_and_send_keys(MobileBy.XPATH, xpath_expr, content)

    def screenshot(self,picture_path):
        self.driver.save_screenshot(picture_path)
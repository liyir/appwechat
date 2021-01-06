import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __int__(self, base_driver=None):
        #注解，不是赋值操作.用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    # #获取cookie,序列化后存入yaml文件内
    # def test_get_cookie():
    #     # 复用浏览器
    #     opt = webdriver.ChromeOptions()
    #     # 设置debug地址
    #     opt.debugger_address = "127.0.0.1:9222"
    #     driver = webdriver.Chrome(options=opt)
    #     driver.implicitly_wait(5)
    #     driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    #     cookie = driver.get_cookies()
    #     print(cookie)
    #     with open("cookie.yml", "w", encoding="UTF-8") as f:
    #         yaml.dump(cookie, f)

    def __cookie_login(self):
        #使用cookie登录
        with open("cookie.yml", encoding="UTF-8") as f:
            yaml_cookie = yaml.safe_load(f)  # 读取yaml里的信息赋给yaml_cookie
            for cookie in yaml_cookie:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    #在底层封装find_element()方法
    def find(self,by,value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self,by,value=None):
        if value is None:
            # 如果传入的是一个元组，则进行解包元组传参
            return self.driver.find_elements(*by)
        else:
            #如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=value)

    def wait_click(self,locator):
        return WebDriverWait(self.driver, 9).until(
            expected_conditions.element_to_be_clickable(locator))


    def quit(self):
        """
        退出二次封装
        :return:
        """
        self.driver.quit()
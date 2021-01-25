# 启动类的操作
from appium import webdriver

from testframe.base_page import BasePage
from testframe.pages.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            # noReset 保留缓存， 比如登录状态
            caps["noReset"] = "true"
            # 设置页面等待空闲状态的时间
            caps['settings[waitForIdleTimeout]'] = 0
            # 关键  localhost:4723  本机ip:server端口
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()

        # self.driver.start_recording_screen("./tmp.mp4")
        # 操作，在 10 内，每 0.5 s 查找一次元素
        self.driver.implicitly_wait(10)

    # app通过goto_main方法，把driver方法传给mainpage，mainpage拿到driver才能进行点击操作
    def goto_main(self):
        return MainPage(self.driver)
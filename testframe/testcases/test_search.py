from testframe.app import App


class TestSearch:
    def setup(self):
        self.app=App()
    def test_search(self):
        """
        搜索测试用例
        :return:
        """
        self.app.start()
        self.app.goto_main().goto_market().goto_search().search()
import pytest

from pages.main_page import MainPage

#只在cases内添加断言，方法内不添加断言
class TestAddMember:
    def setup_class(self):
        #第一次实例化
        self.main=MainPage()

    def test_add_member(self):
        """
        添加成员测试用例
        :return:
        """
        #1.跳转添加成员页面；2.添加成员；3.自动跳转到通讯录页面
        res = self.main.goto_add_member().add_member().get_member_list()
        assert "哈2" in res


    @pytest.mark.parametrize("acctid,phone,expect_res",
                             [("ha1","13758572334","该账号已被”哈1“占有"),
                              ("ha3","18867105766","该手机号已被”那个谁“占有")])
    #第一次参数化，传入重复的acctid,正确的phone和断言信息
    #第二次参数化，传入正确的acctid,重复的phone和断言信息
    def test_add_member_fail(self,acctid ,phone,expect_res):
        """
        添加成员失败测试用例
        :param acctid:id信息
        :param phone:手机信息
        :param expect_res：断言信息
        :return:
        """
        res = self.main.goto_add_member().add_memeber_fail(acctid,phone)
        assert expect_res in res

    def test_add_member_by_contact(self):
        """
        通过通讯录添加成员用例
        :return:
        """
        #跳转通讯录页面；2.添加成员
        res = self.main.goto_contact().goto_add_member().add_member().get_member_list()
        assert "哈2" in res

    #回到首页，还原一开始的状态
    def teardown(self):
        self.main.back_main()

    # def teardown_class(self):
    #     self.main.quit()


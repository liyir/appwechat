from testapp.pages.app import App


def test_add_member():
    """
    手动添加成员测试用例
    :return:
    """
    app = App()
    app.start()
    result = app.goto_main().goto_address_list().goto_add_member().add_member_manual().add_contact()
    assert result





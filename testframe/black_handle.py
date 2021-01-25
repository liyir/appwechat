# 装饰器
import logging

import allure
logging.basicConfig(level=logging.INFO)
# error>info>debug


def black_wrapper(fun):
    """
    《python cookbook》
    :param fun:
    :return:
    """
    def run(*args, **kwargs):
        basepage = args[0]  # 接self  self作为第0个参数被传递给basepage
        try:
            logging.info("start find:\nargs:" + str(args)+ "\nkwargs:" + str(kwargs))
            return fun(*args, **kwargs)  # 闭包
        # 捕获元素没找到异常
        except Exception as e:
            # 截图记录到allure
            basepage.screenshot("tmp.png")
            with open("./tmp.png",'rb') as f:  # rb: 以二进制格式打开一个文件用于只读
                picture_data=f.read()
            allure.attach(picture_data,attachment_type=allure.attachment_type.PNG)
            #遍历黑名单中的元素，进行处理
            for black in basepage.black_list:
                eles = basepage.finds(*black) # 对元组进行解包
                # 如果黑名单被找到，进行相应操作
                if len(eles)>0:
                    # 对黑名单元素进行点击，可以进行其他操作，根据业务来封装操作
                    eles[0].click()
                    return fun(*args,**kwargs)
            raise e
    return run

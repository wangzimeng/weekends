# 有了myTestCase以后，在写测试用例不需要重写setup，tearDown方法
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    # 三个双引号，表示文档字符串，也是一种注释，和#区别就算这种注释会显示在文档中
    """注册模块测试用例"""
    # 因为MyTestCase已经实现了setup，tearDown方法，以后再写测试用例不需要重新实现
    def test_zhu_ce(self):
        """打开注册页面测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")

        # driver.current_url  # 用来获取当前浏览器网址
        actual = driver.title # 用来获取当前浏览器中的标签页title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        # 截取整个浏览器的图片
        base_path = os.path.dirname(__file__)
        path = base_path.replace("day5", "report/image/")
        print(path)
        driver.get_screenshot_as_file(path + "zhuce.png")
        self.assertEqual(actual, expected)


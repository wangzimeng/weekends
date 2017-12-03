import unittest

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class DengLuTest(unittest.TestCase):
    """登陆模块测试用例"""
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # driver.maximize_window()

    def tearDown(self):
        time.sleep(30)
        self.driver.quit()

    def test_denglu(self):
        """登陆测试正常情况测试用例"""
        driver = self.driver
        driver.get("http://localhost/admin.php")
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(
            Keys.ENTER).perform()

        print("用户名：admin  密码：123456")






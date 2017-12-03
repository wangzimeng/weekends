import unittest

import time
from selenium import webdriver


class MemberManageTest(unittest.TestCase):
    # 变量前面加上self.表示这个变量是类的属性，可以被所有的方法访问
    def setUp(self):
        # 打开浏览器
        # driver声明在setUp方法之内，不能被其他方法访问
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # driver.maximize_window()

    def tearDown(self):
        # quit()退出浏览器
        # close() 关闭一个浏览器页签
        # 代码编写和调试的时候需要在quit()前加时间等待
        # 正式运行的时候去掉时间等待，为了提高程序执行速度
        time.sleep(20)
        self.driver.quit()

    def test_add_member(self):
        driver = self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_name("userverify").submit()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_css_selector(" ul:nth-child(3) > li:nth-child(3) > a").click()
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("test")
        driver.find_element_by_name("mobile_phone").send_keys("13763532521")
        driver.find_element_by_name("sex").click()
        driver.find_element_by_id("birthday").send_keys("1992-11-01")
        driver.find_element_by_name("email").send_keys("karry@qq.com")
        driver.find_element_by_name("qq").send_keys("123145512")
        driver.find_element_by_name("qq").submit




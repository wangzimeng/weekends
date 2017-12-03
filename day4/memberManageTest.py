import unittest

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from day4.readCsv2 import read
# 1.导入ddt代码库
import ddt


# 2.装饰这个类
@ddt.ddt

class MemberManageTest(unittest.TestCase):
    # 3.调用之前写好的rea()方法，获取配置文件中的数据
    member_info = read("goods_info.csv")
    global driver
    # 当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前，只执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("登陆测试")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()

    # python中集合前面的星号表示把集合中的所有元素拆开一个一个写
    # list = ["karry","wang"]
    # *list = "karry","wang"
    # *的作用把列表拆成两个string
    # 假如一个方法接收两个参数，不能传一个list进去
    # 但是如果list中正好两个元素，这时在列表前面加*就可以传进去，这时就不认为这是一个列表，而是两个参数
    # 5.@ddt.data()测试数据来源于read()方法
    # 把数据表中的每一行传入方法，在方法里面增加一个参数row
    @ddt.data(*member_info)
    def test_b_add_member(self, row):
        # print("添加会员")
        driver = self.driver
        # 每组测试数据就算一条测试用例，每条测试用例是独立的，不能因为上一组数据执行失败，导致下一组数据不能被正常执行，所以不推荐for循环
        # 应该用ddt装饰器，取修饰方法达到用例独立执行的目的
        # ddt  数据驱动测试

        # for row in read("goods_info.csv"):
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        # 如果frame没有name属性时，我们可以通过其他方式定位iframe，把定位好的页面元素传给方法也可以实现切换
        iframe_css = "#mainFrame"
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.execute_script('document.getElementsByName("sex")', row[2])
        # driver.find_element_by_css_selector('[value="0"]')
        driver.find_element_by_name("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_css_selector('[value="提交"]').click()

        # 之前代码是能够自动运行，但是还不能自动判断程序运行的是否正确，我们自动化代码不能找人一直盯着运行，检查是否执行报错
        # actualz实际结果,执行测试用例之后，页面上实际显示的结果
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        # expected 期望结果，来自于手动测试用例，需求文档
        expected = row[0]
        # 断言类似于if。。。else语句，用来做判断
        # if actual == expected:
        #     print("测试通过")
        # else:
        #     print("测试失败")
        # 断言assert,断言是框架提供的，要想调用断言，必须加上self，因为测试用例类继承了框架中的TestCase类，也继承了这个类中的断言，所以我们可以直接使用


        # 切换到父框架
        driver.switch_to.parent_frame()
        # 切换到网页的根节点
        # driver.switch_to.default_content()
        # 断言有几个特点：
        # 1.断言简短
        # 2.断言只关注错误的测试用例，只有判断为假才有报错信息
        # 3.断言报错时，后面代码将不会继续执行，前面步骤失败，后面步骤就不需要尝试了
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()




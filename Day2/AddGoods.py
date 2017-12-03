# 1.登陆
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_class_name("captcha").send_keys("1234")
driver.find_element_by_class_name("captcha").submit()
time.sleep(3)

# 2.商品管理
driver.find_element_by_link_text("商品管理").click()

# 3.添加商品
driver.find_element_by_link_text("添加商品").click()

# 4.商品名称
# 有一种特殊的网页，比如左边上边有一个导航条，这事就要注意
# 开发喜欢在一个页面嵌套多个页面
# 其中”商品管理"和“添加商品”属于根节点的网页
# 商品名称属于frame框架里的子网页
# 之前讲过窗口切换，用于不同页面之间的页面切换
# 现在也需要切换网页
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone x")
time.sleep(3)

# 5.商品的分类
driver.find_element_by_id("1").click()
# driver.find_element_by_id("2").click()
driver.find_element_by_xpath('//*[@id="2"]').click()
driver.find_element_by_id("6").click()

# 双击是特殊的元素的操作，被封装到ActionChains这个类中
# 链表必须以perform方法作为结尾
driver.find_element_by_id("7").click()
ActionChains(driver).double_click(driver.find_element_by_id("7").click()).perform()
driver.find_element_by_id("jiafen").click()

# 6.商品品牌
# driver.find_element_by_css_selector('[value="0"]').click()
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_index(1)
# 7.提交
# driver.find_element_by_class_name("button_search")
brand.submit()


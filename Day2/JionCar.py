import time

from selenium import webdriver

# 45以下的firefox浏览器，不需要驱动文件
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# 隐式等待，一经设置，对后面语句都有效果，所以创建浏览器时设置一次就可以了
# implicitly_wait() 含蓄，委婉的意思
driver.implicitly_wait(30)
# driver.maximize_window()

driver.get("http://localhost/")
# 在点击登陆按钮之前，我们需要先删除target属性
# 但是js定位比selenim麻烦
# 可不可以用selennium的定位方式来替换js
# 用arguments关键字，把元素定位作为一个参数，替换到js语句中
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')", login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("wangzimeng")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("password").submit()
# submit()用于提交form表单。form事故html中的一个元素
# form表单任何一个子孙节点都可以调用submit()方法提交表单
# time.sleep(5)
# time.sleep到底设成几秒比较好
# 用隐式等待，会自动判断网页是否加载完毕，加载完毕立刻执行后面的操作
# 需要设置最大时间，不能让程序无限等待，一般这个时间是30s
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
# iphon_img = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
iphone_link = "div.shop_01-imgbox > a"
# 因为我们copy的是selector，所以要用css selector方式定位
# img是标签名，>前面是父节点，后面是子节点
# 如果想在css中写class属性，那么前面需要加上点
# :nth-child(2),表示当前节点在家中排行老二，是他父亲的第二个儿子
# 为什么把css selector中的内容改的越短越好？
# 涉及到越多的网页元素，代码健壮性和可维护性越差
# 因为开发一旦修改页面时，修改了你涉及到的节点，元素就会定位失败
iphone = driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')", iphone)
iphone.click()

# 点击加入购物车
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
time.sleep(5)
# 点击添加新地址
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("karry")
driver.find_element_by_name("address[mobile]").send_keys("13318878901")
# 添加收货地区
driver.find_element_by_id("add-new-area-select").click()
driver.find_element_by_css_selector("[value='230000']").click()
driver.find_element_by_css_selector('[value="230200"]').click()
driver.find_element_by_css_selector('[value="230230"]').click()

# 收货地区
# 定位第一个下拉框
# Sheng = driver.find_element_by_id("add-new-area-select")
# Select(Sheng).select_by_value("230000")
# 定位第二个下拉框
# Shi = driver.find_elements_by_tag_name("select")[1]
# Select(Shi).select_by_index(2)
# 定位第三个下拉框
# Xian = driver.find_elements_by_tag_name("select")[2]
# Select(Xian).select_by_visible_text("克东县")

# 详细地址
driver.find_element_by_name("address[address]").send_keys("北京")
# 邮编
driver.find_element_by_name("address[zipcode]").send_keys("10086")
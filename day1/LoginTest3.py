# javascript 是一门独立的语言
# 学好selenium三件事:
# 1.元素的定位 id--name--class
# link_test必须是链接，必须是<a>标签，必须是文本
# 第五种 js selector
# 2.元素的操作：鼠标单机click，发送键盘按键send_keys
# 3.学好javascript
#
# 用javascript 实现窗口切换
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/")
# javascript和python是不同语言
js = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)
# 点击登陆链接
driver.find_element_by_link_text("登录").click()
# 输入用户名密码
driver.find_element_by_id("username").send_keys("wangzimeng")
driver.find_element_by_id("password").send_keys("123456")
# 点击登陆按钮
driver.find_element_by_class_name("login_btn").click()

img = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"

driver.find_elements_by_xpath(/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img)


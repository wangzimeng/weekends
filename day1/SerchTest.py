# 1.登陆
# 2.返回商城首页
# 3.搜索商品
# 4.选择商品
# 5.加入购物车
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("登录").click()
cwh = driver.current_window_handle
whs = driver.window_handles
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_id("username").send_keys("wangzimeng")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("login_btn").click()
time.sleep(5)
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
img = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
driver.find_element_by_css_selector(img).click()
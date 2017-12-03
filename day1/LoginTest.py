# 1.打开浏览器
from selenium import webdriver
# 从selenium 导入网络驱动，用来操作浏览器
driver = webdriver.Chrome()
# 2.打开登陆页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 3.输入用户名,寻找用户名的输入框
# 网页所有可见的都是element
# 在叫driver的浏览器上，寻找一个网页元素，如果它的id =“username”
# 并且像页面元素中发送键盘上“wangzimeng"的按键
driver.find_element_by_id("username").send_keys("wangzimeng")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("login_btn").click()


# 注册
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("karry")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("13678112364")
driver.find_element_by_name("email").send_keys("l123142@163.com")
driver.find_element_by_class_name("reg_btn").click()

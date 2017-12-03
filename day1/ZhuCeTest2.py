# 1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
# 2.打开商城网页
# 网址必须包含协议信息
driver.get("http://localhost/")
# 3.点击注册连接
# 三种元素定位 id name class
# 第四种元素定位方法“连接的文本信息
driver.find_element_by_link_text("注册").click()
# 4.窗口切换：把selenium切换到新的窗口工作
cwh = driver.current_window_handle  # 浏览器当前窗口的句柄
# selenium只提供了工作窗口的名字，并没有提供第二个窗口的名字，我们自己求
whs = driver.window_handles   # 浏览器中所有当前窗口的句柄
# for关键字 集合中的某个元素 in关键字  数组（集合）
# 所以item表示whs中的一个元素，每次循环取一个值，循环结束
# whs中的每个元素都会被遍历一次
for item in whs:
    if item == cwh:
        pass  # 跳过不执行
        # driver.close()  # 关闭当前标签
    else:
        # 把selenium切换到第二个窗口
        driver.switch_to.window(item)  # 这种情况就是要找的窗口了

driver.find_element_by_name("username").send_keys("karry")
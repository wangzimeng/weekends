# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("wangzimeng")
# Chains链表和数组不同，数组有固定长度，链表必须有明确的结束标志perform
# 对整个浏览器转换ActionChains类型
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()

# 2.点击账号设置
driver.find_element_by_link_text("账号设置").click()

# 3.点击个人资料
# 部分testlink
driver.find_element_by_partial_link_text("个人资料").click()

# 4.修改个人信息
# clear 用来清除元素中原本的内容
# 更好的编程习惯，在每次执行sendkeys之前都进行clear操作
# css其他值用[]
# css可以用多个属性组合定位一个元素
# 一个元素的多个属性之间不能存在空格，空格表示父子级
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("王子")
driver.find_element_by_css_selector('#xb[value="2"]').click()

# js是单独语言，和python的语法不一样
# js = 'document.getElementById("date").removeAttribute("readonly")'
# driver.execute_script(js)
# driver.find_element_by_id("date").clear()
# driver.find_element_by_id("date").send_keys("2016-11-25")

# 用arguments改写上面输入。用selenium的定位方式，定位元素之后，对元素执行js脚本,删除readonly属性
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")', date)
date.clear()
date.send_keys("2016-11-25")

# 用selenium调用js，一共有两个关键字:#  1.arguments[0] 用python语言代替一部分
# 好处是有时selenium定位比较容易
# 2.return 把js的执行结果返回给python
# 好处是selenium定位不到的元素可以用js定位到
# date = diver.execute_script('return document.getElementById("date")')
# 这句话等于 date = driver.find_element_by_id("date")
# date.click()
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("12314124")
driver.find_element_by_id("qq").submit()

# 这种右键检查不了html代码的弹出框交错alert，有单独的方法来处理
time.sleep(3)
# alert控件不是html代码生成的，所以implicitly对这个控件不管用
# 所以就算上面写了implicitl_wait，这个time.sleep（）方法不能省略
# 切换到alert的方法，和切换窗口的方法类似
# alert 弹出框，accept 接受，同意 dismiss拒绝，取消
driver.switch_to.alert.accept()
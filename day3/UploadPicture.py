# 1.登陆
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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
driver.find_element_by_xpath('//*[@id="1"]').click()
# driver.find_element_by_css_selector("#2")
driver.find_element_by_css_selector("[id='2']").click()
driver.find_element_by_id("6").click()
# driver.find_element_by_id("7").click()

# 双击是特殊的元素的操作，被封装到ActionChains这个类中
# 链表必须以perform方法作为结尾
driver.find_element_by_id("7").click()
ActionChains(driver).double_click(driver.find_element_by_id("7").click()).perform()
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_index(1)

# 6.商品品牌
# driver.find_element_by_css_selector('[value="0"]').click()
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_index(1)

# 7.点击商品图册
driver.find_element_by_link_text("商品图册").click()
# 有些页面控件是js在页面加载之后生成的
# implicitily_wait是用来判断整个网页是否加载完毕
# 有时页面加载完，但是js的控件还没有创建好
# 所以需要加一个time.sleep提高程序的稳定性
time.sleep(3)
driver.find_element_by_css_selector("#filePicker label")
# 因为真正负责上传的文件的页面元素是<input type="file"
# 所以我们可以直接操作这个控件
# 这个控件可以直接输入图片的路径
driver.find_element_by_name("file").send_keys("D:/uploder.png")

# 页面太长，点击不了下面的button，怎么操作滚动条
ac = ActionChains(driver)
for i in range(10):
    ac.send_keys(Keys.ARROW_RIGHT)
ac.perform()

# 点击开始上传，同时用三个class定位
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
# alert 这个控件不是立刻弹出来的,需要时间等待
time.sleep(3)
driver.switch_to.alert.accept()

# 7.提交
driver.find_element_by_class_name("button_search").click()

# js滚动像素
# driver.execute_script("window.scrollTo(200,100)")

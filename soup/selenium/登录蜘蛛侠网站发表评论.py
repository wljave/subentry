import time
# 从selenium库中调用webdriver模块
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行

# login_name = input('请输入你的用户名或者邮箱地址：')
# login_pwd = input('请输入你的密码：')

# 设置引擎为Chrome，真实地打开一个Chrome浏览器
# driver = webdriver.Chrome()
# 访问页面
login_url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
driver.get(url=login_url)
# 暂停两秒，等待浏览器缓冲
time.sleep(2)

# 获取完整渲染的网页源代码
pageSource = driver.page_source
# 打印pageSource的类型
# print(type(pageSource))
# 打印pageSource
# print(pageSource)

# 找到【输入账号】下面的输入框位置
text = driver.find_element_by_id('user_login')
# 输入文字
text.send_keys('manpeople')
# 找到【输入密码】下面的输入框位置
password = driver.find_element_by_id('user_pass')
# 输入文字
password.send_keys('X6sfD9loEM7@!EfP')
# time.sleep(1)
# 找到【记住我的登录信息】下面的输入框位置
rememberme = driver.find_element_by_id('rememberme')
# 点击【记住我的登录信息】按钮选择框
rememberme.click()
# time.sleep(1)
# 找到【提交】按钮
button = driver.find_element_by_name('wp-submit')
# 点击【提交】按钮
button.click()
time.sleep(1)

# 跳转人人都是蜘蛛侠页面，找到文章 未来已来（三）——同九义何汝秀
entry_title = driver.find_element_by_partial_link_text('同九义何汝秀')
# 点击【超链接】
entry_title.click()
# 滚动滑轮至最后
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(1)
# 找到【评论】下面的输入框位置
textarea = driver.find_element_by_name('comment')
# 输入文字
# textarea.send_keys(input('请输入评论内容：'))
textarea.send_keys('第五次使用selenium进行评论了')
# 找到【发表评论】按钮
submit = driver.find_element_by_name('submit')
# 点击【发表评论】按钮
submit.click()
time.sleep(1)

print('使用selenium评论成功！')
# 关闭浏览器
driver.close()



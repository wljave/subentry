# *******本地Chrome浏览器设置方法**********
# 从selenium库中调用webdriver模块
from selenium import webdriver
# 调用时间模块
import time

# 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver = webdriver.Chrome()
# 访问页面
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# 暂停两秒，等待浏览器缓冲
time.sleep(2)

# 获取完整渲染的网页源代码
pageSource = driver.page_source
# 打印pageSource的类型
print(type(pageSource))
# 打印pageSource
print(pageSource)

# 找到【请输入你喜欢的老师】下面的输入框位置
# teacher = driver.find_element_by_id('teacher')
# 输入文字
# teacher.send_keys('必须是吴枫呀')
# 找到【请输入你喜欢的助教】下面的输入框位置
# assistant = driver.find_element_by_name('assistant')
# 输入文字
# assistant.send_keys('都喜欢')
# time.sleep(1)
# # 解析网页并提取<label>标签
# labels = driver.find_elements_by_tag_name('label')
# # 打印label的文本
# for item in labels:
#     print(item.text)
# 找到【提交】按钮
# button = driver.find_element_by_class_name('sub')
# time.sleep(1)
# 点击【提交】按钮
# button.click()
# time.sleep(1)
# 关闭浏览器
driver.close()

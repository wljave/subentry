import time
from bs4 import BeautifulSoup
# from selenium import webdriver
# ************本地Chrome浏览器的静默默模式设置：**************
from selenium import webdriver  # 从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行

# driver = webdriver.Chrome()
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/87.0.4280.88 Safari/537.36 ',
# }
# # 设置代理IP
# proxy = '150.138.253.71:808'
# proxies = {'http': 'https://' + proxy}
url = 'https://y.qq.com/n/yqq/song/000kbQ6l3srzE5.html'

driver.get(url=url)
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot')  # 根据类名找到【点击加载更多】
button.click()  # 点击
time.sleep(2)  # 等待两秒

# **********方法一**************
# comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')  # 使用class_name找到评论
# print(len(comments))
# for comment in comments:  # 循环
#     sweet = comment.find_elements_by_tag_name('p')  # 找到评论
#     for item in sweet:
#         print('评论：%s\n ---\n' % item.text)  # 打印评论
# # pageSource = driver.page_source
# driver.close()

#  ****************方法二 ****************
pageSource = driver.page_source  # 获取Elements中渲染完成的网页源代码
soup = BeautifulSoup(pageSource, 'html.parser')  # 使用bs解析网页
comments = soup.find('ul', class_='js_hot_list').find_all('li', class_='js_cmt_li')  # 使用bs提取元素
print(len(comments))  # 打印comments的数量

for comment in comments:  # 循环
    sweet = comment.find('p')  # 提取评论
    print('评论：%s\n ---\n' % sweet.text)  # 打印评论
driver.close()  # 关闭浏览器 # 关闭浏览器

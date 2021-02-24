# ***************************方法一*******************************
from selenium import webdriver  # 从selenium库中调用RemoteWebDriver模块
from selenium.webdriver.chrome.options import Options  # 调用Option模块
import time

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 把Chrome设置为静默模式
driver = webdriver.Chrome(options=chrome_options)  # 设置浏览器引擎为远程浏览器

url = 'https://localprod.pandateacher.com/python-manuscript/hello-spiderman/show'
driver.get(url)
time.sleep(1)

content = driver.find_elements_by_class_name('content')
for item in content:
    print(item.text)

driver.close()


# ***************************方法二*******************************
from selenium import webdriver  # 从selenium库中调用RemoteWebDriver模块
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
from bs4 import BeautifulSoup
import time

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 把Chrome设置为静默模式
driver = webdriver.Chrome(options=chrome_options)  # 设置浏览器引擎为远程浏览器

url = 'https://localprod.pandateacher.com/python-manuscript/hello-spiderman/show'
driver.get(url)
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content = soup.find_all(class_='content')
for item in content:
    print(item.text)

driver.close()

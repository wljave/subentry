import time
import requests
from bs4 import BeautifulSoup
from urllib.request import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行

name = input('请输入您要下载的电影名称：')
film_name = quote(name.encode('gbk'))
print(name + '=' + film_name)

# 定义要爬取的链接
url = 'http://s.ygdy8.com/plus/s.php?typeid=1&keyword=' + film_name
# 模拟浏览器请求数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 '
}
# 设置代理IP
proxy = '221.122.91.76:9480'
# 需要认证的代理可以写成如下格式，username为用户名，password为密码
# proxy = "username:password@ip:端口号"
proxies = {
    'https': 'https://' + proxy,
}
res = requests.get(url, proxies=proxies, headers=headers)
# 判断状态码是否正常
print(res.status_code)

# 1以网页源代码的格式获取数据
html = res.text
# 2解析数据
soup = BeautifulSoup(html, 'html.parser')
# 3提取数据
items = soup.find(class_='co_content8').find_all('table')
# 定义全局变量
# global href
# for item in items:
# 获取电影名为：film_name的详细页面内含下载链接
if items:
    href = items[0].find('a')['href']
    # 拿到下载页面链接之后，继续提取下载链接
    download_url = 'https://www.ygdy8.com' + href
    print('电影《' + name + '》的下载页面链接为：\n' + 'https://www.ygdy8.com' + href)
    driver.get(url=download_url)
    # 暂停两秒，等待浏览器缓冲
    time.sleep(2)
    # 获取完整渲染的网页源代码
    pageSource = driver.page_source
    # # 模拟浏览器发起请求
    # response = requests.get(download_url, proxies=proxies, headers=headers)
    # # 判断状态码是否正常
    # print(response.status_code)
    # # 设置网页编码方式
    # response.encoding = 'gbk'
    # # 以网页源代码格式，获取数据
    # download_html = response.text
    # 解析数据
    parse = BeautifulSoup(pageSource, 'html.parser')

    # 提取数据
    abstraction = parse.find_all('td', bgcolor='#fdfddf')
    for ftp in abstraction:
        title = ftp.find('a')
        print(title)
        print(type(title))
        # print('复制链接推荐使用迅雷下载：\n'+title.text)
else:
    print('没有' + name + '的链接')

driver.quit()

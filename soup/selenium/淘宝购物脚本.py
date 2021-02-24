import time
import datetime
import requests
import pyautogui as pg
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('-–user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, '
                            'like Gecko) Chrome/71.0.3578.98 Safari/537.36')  # 设置浏览器窗口大小.
# chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
# driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行
# 创建chrome对象并传入设置信息.
driver = webdriver.Chrome(chrome_options=chrome_options)

# 访问页面
login_url = 'https://login.taobao.com/'
# 获取数据
# soup = header(url=login_url)
driver.get(login_url)
# 暂停两秒，等待浏览器缓冲
time.sleep(1)
# 最大化浏览器
driver.maximize_window()
# 获取完整渲染的网页源代码
pageSource = driver.page_source

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x,y = pg.position()
#         positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

# pg.position(x=1472, y=3)
pg.moveTo(1472, 340, 1)
pg.click()
pg.moveTo(1320, 490, 1)
pg.click(button='right')
pg.moveTo(1350, 530, 1)
pg.click()
pg.moveTo(480, 1055, 1)
pg.click()
pg.hotkey('ctrl', 'v')
pg.press('enter')

# # 找到扫码按钮
# icon_qrcode = driver.find_element_by_class_name('login-tip')
# # 点击进行扫码登录
# icon_qrcode.click()


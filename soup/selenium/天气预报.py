import datetime
import threading
import time
# smtplib 用于邮件的发信动作
import smtplib
import requests
# 引入schedule定时模块
import schedule
# import pyautogui
from bs4 import BeautifulSoup
# 用于构建邮件头
from email.header import Header
# 从selenium库中调用webdriver模块
from selenium import webdriver
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 从options模块中调用Options类
from selenium.webdriver.chrome.options import Options

# 城市名称
city_name = []
# 时间
tim_list = []
# 温度
tem_list = []
# 状态
wea_list = []
# 风力
win_list = []
# 风向
wind_list = []
wind_two_list = []
wind_one_list = []
# ******生活指数********
# 指数
cold_list = []
colds_list = []
# 生活状态
state_list = []
# 状态星星数
star_list = []
# 温馨提示
warn_list = []

# names = ['洛阳', '深圳']
names = '洛阳'
# 发送方的邮箱地址 '540247580@qq.com'
# from_addr = input('请输入发件人邮箱：')
from_addr = '540247580@qq.com'
# fejihyezqzarbajg # 邮箱提供的授权码，可在第三方登录。
# maile_password = input('请输入%s邮箱授权码：' % from_addr)
maile_password = 'bbtyakjogxdybdda'
# 'xiaofei2025@163.com'
# to_addr = input('请输入收件人邮箱：')
# to_addrs = ['xiaofei2025@163.com', '2766651786@qq.com']
to_addr = 'xiaofei2025@163.com'


# # 清空系统时间
# date_time = ''


def header(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36'}
    # 设置代理IP
    proxy = '171.97.15.9:8080'  # 221.122.91.76:9480
    # 需要认证的代理可以写成如下格式，username为用户名，password为密码
    # proxy = "username:password@ip:端口号"
    proxies = {
        'https': 'https://' + proxy,
    }
    res = requests.get(url=url, proxies=proxies, headers=headers)
    return res


def city_number(name):
    chrome_options = Options()
    # 把Chrome浏览器设置为静默模式
    chrome_options.add_argument('--headless')
    # 设置引擎为Chrome，在后台默默运行
    driver = webdriver.Chrome(options=chrome_options)

    # 访问页面
    find_url = 'http://www.weather.com.cn/forecast/'
    # 获取数据
    driver.get(url=find_url)
    # 暂停两秒，等待浏览器缓冲
    time.sleep(1)
    # 获取完整渲染的网页源代码
    pageSource = driver.page_source

    # 找到【输入城市的输入框位置】输入城市、乡镇、街道、景点名称 查天气
    text = driver.find_element_by_class_name('textinput')
    # 输入文字
    text.send_keys(name)
    time.sleep(2)
    # 找到【下拉列表中的第一个选项】
    show = driver.find_element_by_id('show').find_element_by_tag_name('li')
    # 将属性中的值提取出来
    num = show.get_attribute('num')
    # print('天气预报' + '\n' + '编号:' + num)
    # 关闭浏览器
    driver.quit()
    return num


def res_soup(name):
    num = city_number(name)
    url = 'http://www.weather.com.cn/weather/' + num + '.shtml'
    res = header(url=url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def index_of_living(soup):
    # soup = res_soup()
    # 找到【生活指数】
    hots = soup.find(class_='hide show').find_all('li')
    # print(hots)
    for hot in hots:
        # 状态
        state = hot.find('span')
        state_list.append(state.text.strip())
        # 指数
        colds = hot.find_all('em')
        for coldly in colds:
            cold = coldly.text.strip().replace('中国人民保险', '').replace('健臻·', '')
            cold_list.append(cold)
        # 建议
        warn = hot.find('p')
        warn_list.append(warn.text.strip())

    # 判断减肥指数的星星数
    if '' in state_list:
        stars = soup.find(class_='hide show').find_all('span')
        for star1 in stars:
            star2 = star1.find_all(class_='star')
            for star3 in star2:
                star4 = star3['class']
                star_list.extend(star4)
        # print(len(star_list))
        state_list.remove('')
        state_list.insert(1, str(len(star_list)) + '颗星')
        for t in range(len(star_list)):
            star_list.remove('star')
    for i in range(5):
        cold_list.remove('')
    colds_list.extend(cold_list)
    # print(colds_list)
    # print(state_list)
    # print(warn_list)
    # print(star_list)
    # print('生活指数')
    # for p in range(len(colds_list)):
    #     print('****************************************************************************')
    #     print(colds_list[p] + '：' + state_list[p])
    #     print('温馨提示：' + warn_list[p])
    return colds_list, state_list, warn_list


def weather_forecast(soup):
    # soup = res_soup()
    # 城市
    city = soup.find(class_='crumbs fl').text.replace('\n', '').replace(' ', '').replace('>', ' ')[3:-3]
    city_name.append(city)
    content = soup.find_all(class_='sky')
    for item in content:
        # 时间
        tim = item.find('h1')
        tim_list.append(tim.text)
        # 温度
        tem = item.find(class_='tem')
        tem_list.append(tem.text.strip())
        # 状态
        wea = item.find(class_='wea')
        wea_list.append(wea.text)
        # 风力
        wind = item.find(class_='win')
        win_list.append(wind.text.strip())
        # 风向
        wind_direction = wind.find_all('span')
        for wind_dire in wind_direction:
            win = wind_dire['title']
            wind_list.append(win)

    # print(wind_list)
    # print(win_list)
    if len(wind_list) == 13:
        wind_list.insert(1, wind_list[0])
    for i in range(0, 14, 2):
        wind_two = wind_list[i]
        wind_two_list.append(wind_two)
        i += 1
        wind_one = wind_list[i]
        wind_one_list.append(wind_one)
    # print(wind_two_list)
    # print(wind_one_list)

    # print('城市:' + city.replace('\n', '').replace(' ', '').replace('>', ' ')[3:-3])
    # # print(len(tim_list))
    # for j in range(len(tim_list)):
    #     print('-----------------------------------------')
    #     print('时间:' + tim_list[j])
    #     print('温度:' + tem_list[j])
    #     print('状态:' + wea_list[j])
    #     if '转' not in win_list[j]:
    #         print('风力:' + wind_two_list[j] + win_list[j])
    #     else:
    #         wins = win_list[j].replace('转', ',')
    #         winds = wins.split(',')
    #         if wind_two_list[j] == wind_one_list[j]:
    #             print('风力:' + wind_two_list[j] + winds[0] + '转' + winds[1])
    #         else:
    #             print('风力:' + wind_two_list[j] + winds[0] + '转' + wind_one_list[j] + winds[1])
    #     if j == 0:
    #         print('-----------------------------------------')
    #         index_of_living(soup)
    return city_name, tim_list, tem_list, wea_list, win_list, wind_two_list, wind_one_list


def send_email(num, soup, to_addr, times):
    # 发信服务器
    smtp_server = 'smtp.qq.com'
    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(smtp_server, 465)
    # SMTP服务器地址是：smtp.qq.com，默认端口号25、qq邮箱端口是465或587
    # server.connect(smtp_server, 465)
    # username:登录邮箱的用户名  #password：登录密码/授权码
    server.login(from_addr, maile_password)

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    content_text = ''
    weather_forecast(soup)
    content_text += times + '的天气预报' + '\n' + '编号:' + num + '\n' + '城市:' + city_name[0] + '\n'
    # print(len(tim_list))  每执行一次就会翻倍
    for j in range(7):
        content_text += '------------------------------------------------------------------------------' + '\n'
        content_text += '时间:' + tim_list[j] + '\n' + '温度:' + tem_list[j] + '\n' + '状态:' + wea_list[j] + '\n'
        if '转' not in win_list[j]:
            content_text += '风力:' + wind_two_list[j] + win_list[j] + '\n'
        else:
            wins = win_list[j].replace('转', ',')
            winds = wins.split(',')
            if wind_two_list[j] == wind_one_list[j]:
                content_text += '风力:' + wind_two_list[j] + winds[0] + '转' + winds[1] + '\n'
            else:
                content_text += '风力:' + wind_two_list[j] + winds[0] + '转' + wind_one_list[j] + winds[1] + '\n'
        if j == 0:
            index_of_living(soup)
            content_text += '------------------------------------------------------------------------------' + '\n'
            for p in range(6):
                content_text += colds_list[p] + '：' + state_list[p] + '\n' + '温馨提示：' + warn_list[p] + '\n'
            del state_list[1]
    content_text += '------------------------------------------------------------------------------'

    # print(content_text)
    msg = MIMEText(content_text, 'plain', 'utf-8')

    # *********清空列表***********
    # 时间
    tim_list[:] = []
    # 温度
    tem_list[:] = []
    # 状态
    wea_list[:] = []
    # 风力
    win_list[:] = []
    # 风向
    wind_list[:] = []
    wind_two_list[:] = []
    wind_one_list[:] = []
    # ******生活指数********
    # 指数
    cold_list[:] = []
    colds_list[:] = []
    # 生活状态
    state_list[:] = []
    # 状态星星数
    star_list[:] = []
    # 温馨提示
    warn_list[:] = []

    # 邮件头信息
    msg['from'] = Header('Jave<%s>' % from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(times + '的天气预报', 'utf-8')

    try:
        # 三个参数分别是：发件人邮箱账号，收件人邮箱账号，发送的邮件体
        server.sendmail(from_addr, to_addr, msg.as_string())
        print('电子邮件发送成功!')
    except:
        print('邮件发送失败，请重试！')

    # 退出服务器，结束SMTP会话
    server.quit()


def job1():
    date_time = datetime.datetime.now().strftime("%Y-%m-%d")
    times = date_time[:4] + '年' + date_time[5:7] + '月' + date_time[8:10] + '日'
    print(times + '-任务开始')
    num, soup = city_number(names), res_soup(names)
    send_email(num, soup, to_addr, times)
    print(times + '-任务完成')


# def t1():
#     t = threading.Thread(target=job1)
#     t.start()
#
#
# def t2():
#     t = threading.Thread(target=job2)
#     t.start()


# schedule.every(2).seconds.do(job)        # 每2s执行一次job()函数
# schedule.every(10).minutes.do(job)       # 部署每10分钟执行一次job()函数的任务
# schedule.every().hour.do(job)            # 部署每×小时执行一次job()函数的任务
# schedule.every().day.at("10:30").do(job) # 部署在 每天的10:30执行job()函数的任务
# schedule.every().monday.do(job)          # 部署每个星期一执行job()函数的任务
# schedule.every().wednesday.at("13:15").do(job)# 部署每周三的13：15执行函数的任务
# schedule.every().wednesday.at("21:57").do(job1)
schedule.every().day.at("07:30").do(job1)

while True:
    schedule.run_pending()
    time.sleep(1)

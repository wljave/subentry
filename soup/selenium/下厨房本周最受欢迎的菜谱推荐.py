# ********爬虫模块********
import requests
from bs4 import BeautifulSoup
# ********发送邮件模块********
# smtplib 用于邮件的发信动作
import smtplib
# 用于构建邮件头
from email.header import Header
# email 用于构建邮件内容
from email.mime.text import MIMEText
# ********定时模块********
# 引入schedule定时模块
import schedule
import time

# 定义列表用来保存遍历后的所有的菜名、所有的URL、所有的食材
menu_title = ''  # 标题
menu_pic_list = []  # 展示图片
menu_name_list = []  # 所有的菜名
menu_materials_list = []  # 所有的食材
menu_url_list = []  # 所有的URL
# 发送方的邮箱地址 '540247580@qq.com'
from_addr = '540247580@qq.com'
# fejihyezqzarbajg # 邮箱提供的授权码，可在第三方登录。
maile_password = 'fejihyezqzarbajg'
# 收件人邮箱地址
# to_addrs = ['xiaofei2025@163.com', '540247580@qq.com', '2386265306@qq.com']
# to_addr = '540247580@qq.com'
to_addrs = ['1582467376@qq.com', '1006777530@qq.com',]


def header(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36'}
    # 设置代理IP
    proxy = '180.128.1.83:8080'  # 221.122.91.76:9480
    # 需要认证的代理可以写成如下格式，username为用户名，password为密码
    # proxy = "username:password@ip:端口号"
    proxies = {
        'http': 'https://' + proxy,
    }
    res = requests.get(url=url, proxies=proxies, headers=headers)
    res.encoding = 'utf-8'
    # 1.以网页源代码的格式获取数据
    html = res.text
    return html


def menu_recommend():
    global menu_title
    for i in range(10):
        # 定义要爬取的网页链接
        url = 'https://www.xiachufang.com/explore/?page=%d' % (i + 1)
        # 2.解析数据
        soup = BeautifulSoup(header(url), 'html.parser')
        # 3.提取数据
        items = soup.find_all(class_='pure-u-3-4 search-result-list')

        # 遍历items获取想要的数据
        for item in items:
            # 菜图片
            picture = item.find_all(class_='cover pure-u')
            for pic in picture:
                menu_pic = pic.find('img')['data-src']
                menu_pic_list.append(menu_pic)
            # 标题
            title = item.find(class_='page-title').text
            menu_title = title.strip()
            # 菜名
            menu_name = item.find_all('p', class_='name')
            for name in menu_name:
                menu_name_list.append(name.text.strip())
            # 所需材料
            menu_materials = item.find_all(class_='ing ellipsis')
            for materials in menu_materials:
                menu_materials_list.append(materials.text.strip())
            # 详情页链接
            for urls in menu_name:
                menu_url = urls.find('a')['href']
                menu_url_list.append(menu_url)

    return menu_pic_list, menu_name_list, menu_materials_list, menu_url_list


def send_email():
    # 发信服务器
    smtp_server = 'smtp.qq.com'
    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL()
    # SMTP服务器地址是：smtp.qq.com，默认端口号25、qq邮箱端口是465或587
    server.connect('smtp.qq.com', 465)
    # username:登录邮箱的用户名  #password：登录密码/授权码
    server.login(from_addr, maile_password)

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    content_text = ''
    # content_text += '标题：' + menu_title + '\n'
    for j in range(len(menu_name_list)):
        content_text += '<p>----------------【点击下方图片查看制作详情】------------------</p>'
        content_text += '<p>图片：' + '<a href=%s><img border="0" src=%s  alt=%s width="215" height="136"/></a></p>' % (('https://www.xiachufang.com' + menu_url_list[j]), menu_pic_list[j], menu_name_list[j])
        content_text += '<p>菜名：%s</p>' % menu_name_list[j]
        content_text += '<p>所需材料：%s</p>' % menu_materials_list[j]
        # content_text += '<a href= %s>点击查看制作详情</a>' % ('https://www.xiachufang.com' + menu_url_list[j])
    # content_text += '<p>-------------------------------------------------------------------</p>'

    # 使用多文本类型
    msg = MIMEText(content_text, 'html', 'utf-8')

    # 邮件头信息
    msg['from'] = Header('Jave<%s>' % from_addr)
    msg['To'] = Header(",".join(to_addrs))
    msg['Subject'] = Header(menu_title, 'utf-8')

    try:
        # 三个参数分别是：发件人邮箱账号，收件人邮箱账号，发送的邮件体
        server.sendmail(from_addr, to_addrs, msg.as_string())
        print('电子邮件发送成功!')
    except:
        print('邮件发送失败，请重试！')

    # 退出服务器，结束SMTP会话
    server.quit()


def work():
    print('work开始任务')
    menu_recommend()
    send_email()
    print('work任务完成')


schedule.every().day.at("11:31").do(work)
# schedule.every().friday.at("13:15").do(work)    # 部署每周五的13：15执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)

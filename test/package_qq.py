import csv
# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 用于构建邮件头
from email.header import Header

# 发送方的邮箱地址 '540247580@qq.com'
from_addr = input('请输入发件人邮箱：')
# fejihyezqzarbajg # 邮箱提供的授权码，可在第三方登录。
maile_password = input('请输入%s邮箱授权码：' % from_addr)

# 收信方邮箱
# to_addrs = ['xiaofei2025@163.com', 'shuhaoxiong@163.com', 'xiaofei2025@126.com']
# to_addrs = []
# while True:
#     to_addr = input('请输入收件人邮箱：')
#     to_addrs.append(to_addr)
#     continues = input('是否继续输入，n退出，任意键继续：')
#     if continues == 'n':
#         break

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''
    亲爱的，你好！
    今天是2020年12月14日 星期一
    我是Python小邮件程序，能遇见你很开心。
    希望学习Python对你不是一件困难的事情！
    人生苦短，我用Python
    下一步我将使用爬虫爬取你需要的文档、视频、图片等等
    期待这一天早点到来。。。
'''

# 待写入csv文件的收件人数据：人名+邮箱
# 记得替换成你要发送的名字和邮箱
data = [['jave', 'xiaofei2025@163.com'], ['shuhaoxiong', 'shuhaoxiong@163.com'], ['xiaofei', 'xiaofei2025@126.com']]
# 写入收件人数据
with open('to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

# 读取收件人数据，并启动写信和发信流程
with open('to_addrs.csv', 'r') as t:
    reader = csv.reader(t)
    for row in reader:
        to_addrs = row[1]

        msg = MIMEText(text, 'plain', 'utf-8')

        # 邮件头信息
        msg['from'] = Header('Jave<%s>' % from_addr)
        # msg['To'] = Header(",".join(to_addrs))
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('邮件测试3')

        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL()

        # SMTP服务器地址是：smtp.qq.com，默认端口号25、qq邮箱端口是465或587
        server.connect('smtp.qq.com', 465)

        # username:登录邮箱的用户名  #password：登录密码/授权码
        server.login(from_addr, maile_password)

        try:
            # 三个参数分别是：发件人邮箱账号，收件人邮箱账号，发送的邮件体
            server.sendmail(from_addr, to_addrs, msg.as_string())
            print('电子邮件发送成功!')
        except:
            print('发送失败，请重试！')

# 退出服务器，结束SMTP会话
server.quit()

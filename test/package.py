import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_email_by_qq(to):
    sender_mail = '540247580@qq.com'
    sender_pass = 'fejihyezqzarbajg'  # 同样是乱打的

    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed')
    # 邮件添加的头尾信息等
    msg_root['From'] = '540247580@qq.com<540247580@qq.com>'
    msg_root['To'] = to
    # 邮件的主题，显示在接收邮件的预览页面
    subject = 'python 发送邮件测试成功'
    msg_root['subject'] = Header(subject, 'utf-8')

    # 构造文本内容
    text_info = 'hello world! 我的第一封自动发邮件'
    text_sub = MIMEText(text_info, 'plain', 'utf-8')
    msg_root.attach(text_sub)

    # 构造超文本
    url = "https://blog.csdn.net/chinesepython"
    html_info = """
    <p>点击以下链接，你会去向一个更大的世界</p>
    <p><a href="%s">点我</a></p>
    <p>我为你感到非常高兴</p>
    """ % url
    html_sub = MIMEText(html_info, 'html', 'utf-8')
    # 如果不加下边这行代码的话，上边的文本是不会正常显示的，会把超文本的内容当做文本显示
    html_sub["Content-Disposition"] = 'attachment; filename="csdn.html"'
    # 把构造的内容写到邮件体中
    msg_root.attach(html_sub)

    # 构造图片
    image_file = open(r'D:\pythonProject\test\photo1.png', 'rb').read()
    image = MIMEImage(image_file)
    image.add_header('Content-ID', '<image1>')
    # 如果不加下边这行代码的话，会在收件方方面显示乱码的bin文件，下载之后也不能正常打开
    image["Content-Disposition"] = 'attachment; filename="red_people.png"'
    msg_root.attach(image)

    # 构造附件
    txt_file = open(r'D:\pythonProject\test\poem.txt', 'rb').read()
    txt = MIMEText(txt_file, 'base64', 'utf-8')
    txt["Content-Type"] = 'application/octet-stream'
    # 以下代码可以重命名附件为hello_world.txt
    txt.add_header('Content-Disposition', 'attachment', filename='hello_world.txt')
    msg_root.attach(txt)

    try:
        sftp_obj = smtplib.SMTP('smtp.qq.com', 25)
        sftp_obj.login(sender_mail, sender_pass)
        sftp_obj.sendmail(sender_mail, to, msg_root.as_string())
        sftp_obj.quit()
        print('电子邮件发送成功!')

    except Exception as e:
        print('发送邮件失败的一个原因')
        print(e)


if __name__ == '__main__':
    # 可以是一个列表，支持多个邮件地址同时发送，测试改成自己的邮箱地址
    to = 'xiaofei2025@163.com'
    send_email_by_qq(to)

# # 引入requests。
# import requests
#
# # 用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies。
# session = requests.session()
# # 把登录的网址赋值给url。
# url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# # 加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫。
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# # 把有关登录的参数封装成字典，赋值给data。
# data = {
#     'log': input('请输入账号：'),  # 'spiderman'  # 写入账户
#     'pwd': input('请输入密码：'),  # 'crawler334566',  # 写入密码
#     'wp-submit': '登录',
#     'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#     'testcookie': '1'
# }
#
# # 在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参数。
# login_in = session.post(url, headers=headers, data=data)
# # login_in = requests.post(url, headers=headers, data=data)
# # 用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in。
# print(login_in.cookies)
# # # 打印login_in
# # cookies = login_in.cookies
# # 提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies。
#
# url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# # 我们想要评论的文章网址。
# data_1 = {
#     'comment': input('请输入你想要发表的评论：'),
#     'submit': '发表评论',
#     'comment_post_ID': '52',
#     'comment_parent': '0'
# }
# comment = session.post(url_1, headers=headers, data=data_1,)
# # 把有关评论的参数封装成字典。
# # comment = requests.post(url_1, headers=headers, data=data_1, cookies=cookies)
# # 用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment。
# # 调用cookies的方法就是在post请求中传入cookies=cookies的参数。
# print(comment.status_code)
# # 打印出comment的状态码，若状态码等于200，则证明我们评论成功。


# import requests
# import json
#
# session = requests.session()
# # 创建会话。
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/70.0.3538.110 Safari/537.36 '
# }
# # 添加请求头，避免被反爬虫。
# try:
#     # 如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论。
#     cookies_txt = open('cookies.txt', 'r')
#     # 以reader读取模式，打开名为cookies.txt的文件。
#     cookies_dict = json.loads(cookies_txt.read())
#     # 调用json模块的loads函数，把字符串转成字典。
#     cookies = requests.utils.cookiejar_from_dict(cookies_dict)
#     # 把转成字典的cookies再转成cookies本来的格式。
#     session.cookies = cookies
#     # 获取cookies：就是调用requests对象（session）的cookies属性。
#
# except FileNotFoundError:
#     # 如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies，再评论。
#
#     url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
#     # 登录的网址。
#     data = {'log': input('请输入你的账号:'),
#             'pwd': input('请输入你的密码:'),
#             'wp-submit': '登录',
#             'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#             'testcookie': '1'}
#     # 登录的参数。
#     session.post(url, headers=headers, data=data)
#     # 在会话下，用post发起登录请求。
#
#     cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
#     # 把cookies转化成字典。
#     cookies_str = json.dumps(cookies_dict)
#     # 调用json模块的dump函数，把cookies从字典再转成字符串。
#     f = open('cookies.txt', 'w')
#     # 创建名为cookies.txt的文件，以写入模式写入内容
#     f.write(cookies_str)
#     # 把已经转成字符串的cookies写入文件
#     f.close()
#     # 关闭文件
#
# url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# # 文章的网址。
# data_1 = {
#     'comment': input('请输入你想评论的内容：'),
#     'submit': '发表评论',
#     'comment_post_ID': '55',
#     'comment_parent': '0'
# }
# # 评论的参数。
# comment = session.post(url_1, headers=headers, data=data_1)
# # 在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
# print(comment.status_code)
# # 打印comment的状态码


import requests, json

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


def cookies_read():
    cookies_txt = open('cookies.txt', 'r')
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return (cookies)
    # 以上4行代码，是cookies读取。


def sign_in():
    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data = {'log': input('请输入你的账号'),
            'pwd': input('请输入你的密码'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookie': '1'}
    session.post(url, headers=headers, data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    f = open('cookies.txt', 'w')
    f.write(cookies_str)
    f.close()
    # 以上5行代码，是cookies存储。


def write_message():
    url_2 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_2 = {
        'comment': input('请输入你要发表的评论：'),
        'submit': '发表评论',
        'comment_post_ID': '58',
        'comment_parent': '0'
    }
    return session.post(url_2, headers=headers, data=data_2)
    # 以上9行代码，是发表评论。


try:
    session.cookies = cookies_read()
except FileNotFoundError:
    sign_in()

num = write_message()
if num.status_code == 200:
    print('成功啦！')
else:
    sign_in()
    num = write_message()

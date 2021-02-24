import ssl
import requests
from functools import wraps
from bs4 import BeautifulSoup


# 出现ssl证书错误，在网络请求初始化的时候，加入以下代码：
# ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:777)
def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)

    return bar


ssl.wrap_socket = sslwrap(ssl.wrap_socket)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 ',
}
# 设置代理IP
proxy = '150.138.253.71:808'
proxies = {'http': 'https://' + proxy}


# verify=False


def get_bookids():
    books_id = {}
    hot_url = 'https://www.xslou.com/top/allvisit_1/'
    res = requests.get(url=hot_url, headers=headers, proxies=proxies)
    print(res.status_code)
    res.encoding = 'gbk'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    novel_id = soup.find_all('span', class_='up2')
    # print(novel_id)
    for item in novel_id:
        content = item.find('a')
        href = content['href']
        book_name = content.text
        print('小说名：' + book_name)
        print('小说链接：' + href)
        # 字符串link过滤出数字id（9356）
        id_list = list(filter(str.isdigit, href))
        # print(id_list)
        book_id = ''.join(id_list)
        # print(book_id)
        books_id[book_id] = book_name
    return books_id


# 步骤解析：1、filter()过滤数字 2、filter对象转列表 3、列表转字符串
# filter(str.isdigit,字符串)
# 第一个参数用来判断字符串的单个元素是否是数字，数字保留
# filter()返回的是对象，需要用list()函数转换成列表
# ''.join(列表)将列表转换成字符串

# url = 'https://www.xslou.com/yuedu/' + book_id + '/'

# 创建会话
session = requests.session()


def login_cookies():
    global cookies
    # 登录网址
    login_url = ' https://www.xslou.com/login.php'
    # 登录的参数。
    data = {'username': input('请输入你的账号:'),  # 雪妍
            'password': input('请输入你的密码:'),  # 867722
            'action': 'login',
            'redirect_to': 'https://www.xslou.com',
            'usecookie': '1'}
    # 再会话下，用post发起登录请求
    session.post(url=login_url, headers=headers, proxies=proxies, params=data)
    cookies = session.cookies


def urge(book_id):
    urge_url = 'https://www.xslou.com/modules/article/uservote.php?id='
    # 请求推荐链接需要拼接book_id
    url = urge_url + book_id
    # 请求需要带上headers和cookies
    session.post(url, headers=headers, cookies=cookies)
    print('推荐成功！')


def main():
    login_cookies()
    books = get_bookids()
    print('--------热门书籍--------')
    for k, v in books.items():
        print(k, ':', v)
    book_id = input('请输入想要推荐的书籍id：')
    urge(book_id)


main()

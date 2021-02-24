import requests
from bs4 import BeautifulSoup

# 要爬取的网页链接
url = 'http://books.toscrape.com/'
# 1.请求链接
res = requests.get(url)
# 判断状态码是否为200
print('打印状态码：' + str(res.status_code))
# 2.获取数据
html = res.text
# 3.解析数据
soup = BeautifulSoup(html, 'html.parser')
# 4.提取数据
items = soup.find_all(class_='product_pod')
# 遍历items
for item in items:
    # 书名
    books_title = item.find('img')['alt']
    # title = books_title['alt']
    # 评分
    books_grade = item.find('p')['class']
    # 价格
    books_price = item.find(class_='price_color')
    # print(books_title, '\n', books_grade[1], '\n', books_price.text)
    print('书名：' + '《' + books_title + '》')
    if books_grade[1] == 'One':
        print('评分：1分')
    elif books_grade[1] == 'Two':
        print('评分：2分')
    elif books_grade[1] == 'Three':
        print('评分：3分')
    elif books_grade[1] == 'Four':
        print('评分：4分')
    else:
        print('评分：5分')
    # print('评分：' + books_grade[1] + '分')
    print('价格：' + books_price.text[1:])
    # print('\n')


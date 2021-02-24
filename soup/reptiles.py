# import requests
#
# # res = requests.get('https://www.baidu.com')
# # 协议状态码https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md
# # res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# print(type(res))  # <class 'requests.models.Response'>
# print(res)
# # 打印变量res的响应状态码，以检查请求是否成功
# print(res.status_code)
#
# # 把Reponse对象的内容以二进制数据的形式返回
# # pic = res.content
# # with open('ppt.jpg', 'wb') as photo:
# #     photo.write(pic)
#
# # 定义Response对象的编码为gbk
# res.encoding = 'utf-8'
# # 把Response对象的内容以字符串的形式返回
# novel = res.text
# # 现在，可以打印小说了，但考虑到整章太长，只输出800字看看就好。在关于列表的知识那里，你学过[:800]的用法。
# # print(novel[:800])
# with open('《三国演义》.txt', 'a+')as story:
#     story.write(novel)
# print('下载成功')

# import requests
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# print(res.status_code)
# # res.encoding = 'gbk'
# book = res.text
# name = '书苑网页.txt'
# with open(name, 'a+', encoding='utf-8')as bk:
#     bk.write(book)
# print('文件%s下载成功' % name)

# import requests
#
# res = requests.get('http://www.ziliaoh.com/epub.html')
# book = res.text
# with open('图书下载.txt', 'a+', encoding='utf-8')as f:
#     f.write(book)
# print('下载完成')

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
# res = requests.get(url)
# print('打印状态码：' + str(res.status_code))
# html = res.text
# # BeautifulSoup(要解析的文本, 解析器)    <class 'bs4.BeautifulSoup'>
# soup = BeautifulSoup(html, 'html.parser')
# # <class 'bs4.element.Tag'>
# # item = soup.find('div', class_='books')
# # <class 'bs4.element.ResultSet'>
# items = soup.find_all(class_='books')
# for item in items:
#     kind = item.find('h2')
#     title = item.find(class_='title')
#     brief = item.find(class_='info')
#     print('\n', kind.text, '\n', title.text, '\n', title['href'], '\n', brief.text)

# books_name = soup.find_all(class_='title')
# books_info = soup.find_all(class_='info')
# print(type(soup))
# print(type(books_name))
# for item in books_name:
#     print('想找的数据都包含在这里了：\n', item)
#     print(type(item))
# print(books_name)
# print(books_info)

# 调用requests库
import requests
# 调用BeautifulSoup库
from bs4 import BeautifulSoup

url = "http://www.ziliaoh.com/epub.html"
# 返回一个response对象，赋值给res
res = requests.get(url)
# 判断状态码是否正确
print('打印状态码：' + str(res.status_code))
# 把res解析为字符串
book = res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(book, 'html.parser')
# 通过匹配属性class='ite-main'提取出我们想要的元素
items = soup.find_all(class_='site-main')
for item in items:  # 遍历列表items
    title = item.find(class_='entry-title')     # 在列表中的每个元素里，匹配属性class_='title'提取出数据
    contents = item.find(class_='single-content').find_all('p')     # 在列表中的每个元素里，匹配属性<p>标签里面提取出数据
    # content = contents.find_all('p')
    print(title.text)
    for i in contents:
        print(i.text)

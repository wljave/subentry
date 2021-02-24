import time
import requests
from bs4 import BeautifulSoup

# 定义一个列表用来保存公司ID
company_list = []
# 定义编号列表
ranking_id_list = []
# 定义公司名称列表
company_name_list = []


# 头部信息
def header(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36'}
    # 设置代理IP
    proxy = '150.138.253.72:808'
    proxies = {
        'http': 'https://' + proxy,
    }
    res = requests.get(url=url, proxies=proxies, headers=headers)
    return res


# 定义根路径
root_url = 'https://www.jobui.com/company/'
# 比如【深圳市腾讯计算机系统有限公司】
# 定义【公司概况】网址
survey = 'https://www.jobui.com/company/1236/'
# 定义【公司工资】网址
salary = 'https://www.jobui.com/company/1236/salary/'
# 定义【招聘职位】网址
post = 'https://www.jobui.com/company/1236/jobs/'

# 抓取信息路径
url = 'https://www.jobui.com/rank/company/view/shenzhen/'
# 用requests.get()函数抓取网址。
res = header(url=url)
# 请求之后暂停一秒等网页数据
time.sleep(1)
print(res.status_code)
res.encoding = 'utf-8'
# 用requests.get获取网页源代码。
bs = BeautifulSoup(res.text, 'html.parser')
# 用BeautifulSoup解析网页源代码。
datas = bs.find(id='companyList')
# print(datas)
data_companylist = datas['data-companylist']
# 先去掉双引号，再去掉左右两边的列表符号，最后用split()就是将一个字符串分裂成多个字符串组成的列表
id_list = data_companylist.replace('\"', '').strip('[').strip(']').split(',')
# print(id_list)
# print(type(id_list))
company_list.extend(id_list)
print(company_list)

# div最小单元
div_cell = datas.find_all(class_='company-logo-box')

for item in div_cell:
    # 找到排名编号
    ranking_id = item.find('span').text
    if ranking_id != '推广':
        ranking_id_list.append(ranking_id)
        # print(ranking_id)
    else:
        pass
    # 找到公司名
    try:
        company_name = item.find('a')['title']
        company_name_list.append(company_name)
        # print(company_name)
    except TypeError:
        pass


print(ranking_id_list)
print(company_name_list)

for i in range(len(ranking_id_list)):
    # 招聘公司名称
    name = company_name_list[i]
    ids = company_list[i]
    print('【编号】：' + str(i+1))
    print('【公司名称】：' + name)
    # 【公司概况】网址
    print('【公司概况】网址:' + root_url + ids + '/')
    # 【公司工资】网址
    print('【公司工资】网址:' + root_url + ids + '/salary/')
    # 【招聘职位】网址
    print('【招聘职位】网址:' + root_url + ids + '/jobs/')



# # 先将文章内容写进csv文件中
# with open('./amazon/content.csv', 'w', newline='', encoding='utf-8')as file:
#     write = csv.writer(file)
#     for item in datas:
#         # 标题
#         article_title = item.find(class_='article-title').text
#         print('标题：' + article_title)
#         # 作者
#         article_author = item.find(class_='introduce-name').text
#         print('作者：' + article_author)
#         # 文章简介
#         article_summary = item.find(class_='article-summary').text
#         print('文章简介：' + article_summary)
#         # 文章内容
#         article_content = item.find(class_='article-content').text.replace(' ', '')[:-146]
#         print('文章内容：' + article_content)
#         write.writerow(['标题：', article_title])
#         write.writerow(['作者：', article_author])
#         write.writerow(['文章简介：', article_summary])
#         write.writerow(['文章内容：', article_content])
#
#         # 文章中的图片链接
#         content_url = item.find_all(class_='article-content')
#         for p in content_url:
#             images = p.find_all('img')
#             for img in images:
#                 image = img['data-src']
#                 image_url_list.append(image)
# print(image_url_list)
#
# # 定义变量x并初始化用来计数图片的张数
# x = 0
# print('***************************')
# for x in range(len(image_url_list)):
#     # 获取获得的从imglist中遍历得到的imgurl
#     re = requests.get(image_url_list[x])
#     # print(re.status_code)
#     imgres = re.content
#     with open(path + '{}.jpg'.format(x + 1), 'wb') as f:
#         f.write(imgres)
#         x += 1
#         print('正在下载，第', x, '张图片')
# print('图片下载完毕')


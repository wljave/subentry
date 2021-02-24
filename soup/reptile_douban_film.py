# import requests
# import xlsxwriter
# from bs4 import BeautifulSoup
#
#
# def film():
#     for n in range(10):
#         # 定义要爬取的链接
#         url = 'https://movie.douban.com/top250?start=%d&filter=' % (n * 25)
#         # 0.模拟浏览器请求数据
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/87.0.4280.88 Safari/537.36 '
#         }
#         proxy = '39.104.68.232:8080'
#         # 需要认证的代理可以写成如下格式，username为用户名，password为密码
#         # proxy = "username:password@ip:端口号"
#         proxies = {
#             'http': 'https://' + proxy,
#         }
#         res = requests.get(url, proxies=proxies, headers=headers)
#         # 判断状态码是否正常
#         # print(res.status_code)
#
#         # 创建Excel文件
#         wb = xlsxwriter.Workbook('./douban_grade/电影评分.xlsx')
#         # 1获取工作簿
#         sheet = wb.add_worksheet()
#         data = ['电影序号', '电影名', '电影评分', '评价人数', '推荐语', '电影链接']
#         # sheet.append('A1', ['电影序号', '电影名', '电影评分', '评价人数', '推荐语', '电影链接'])
#         sheet.write_row('A1', data)
#
#         # 1.以网页源代码的格式获取数据
#         html = res.text
#         # 2.解析数据
#         soup = BeautifulSoup(html, 'html.parser')
#         # 3.提取数据
#         items = soup.find_all(class_='grid_view')
#         # print(items)
#
#         film_list_all = []
#         film_list_number = []
#         film_list_name = []
#         film_list_grade = []
#         film_list_evaluation_number_people = []
#         film_list_quote = []
#         film_list_url = []
#
#         # 遍历items获取Tag对象
#         for item in items:
#             # 序号
#             film_number = item.find_all(class_='pic')
#             for num in film_number:
#                 number = num.text.strip()
#                 film_list_number.append(number)
#             # print('电影序号：' + str(film_list_number))
#                 sheet.write_column('A2', film_list_number)
#             # 电影名
#             film_name = item.find_all(class_='hd')
#             # film_list.append(film_name.text.replace('\n', '')[:-5])
#             # print('电影名：'+film_name.replace('\n', '')[:-5])
#             for na in film_name:
#                 name = na.text.replace('\xa0', '').replace('\n', '')[:-5]
#                 film_list_name.append(name)
#             # print('电影名：' + str(film_list_name))
#                 sheet.write_column('B2', film_list_name)
#             # 评分
#             film_grade = item.find_all(class_='rating_num')
#             # film_list.append(film_grade.text)
#             # print('电影评分：'+film_grade)
#             for grad in film_grade:
#                 grade = grad.text
#                 film_list_grade.append(grade)
#             # print('电影评分：' + str(film_list_grade))
#                 sheet.write_column('C2', film_list_grade)
#             # 评价人数
#             film_evaluation_number_people = item.find_all(class_='star')
#             # film_list.append(film_evaluation_number_people.text.replace('\n', '')[3:])
#             # print('评价人数：'+film_evaluation_number_people.replace('\n', '')[3:])
#             for enp in film_evaluation_number_people:
#                 evaluation_number_people = enp.text.replace('\n', '')[3:]
#                 film_list_evaluation_number_people.append(evaluation_number_people)
#             # print('评价人数：' + str(film_list_evaluation_number_people))
#                 sheet.write_column('D2', film_list_evaluation_number_people)
#             # 推荐语
#             film_quotes = item.find_all(class_='bd')
#             for f_q in film_quotes:
#                 film_quote = f_q.find_all(class_='quote')
#                 # 判断推荐语是否存在#######################
#                 if not film_quote:
#                     film_list_quote.append('空')
#                     sheet.write_column('E2', film_list_quote)
#                 # film_list.append(film_quote.text.replace('\n', ''))
#                 print('推荐语：'+film_quote.replace('\n', ''))
#                 for quo in film_quote:
#                     quote = quo.text.replace('\n', '')
#                     film_list_quote.append(quote)
#                     sheet.write_column('E2', film_list_quote)
#             # print('推荐语：' + str(film_list_quote))
#
#             # 链接
#             film_url = item.find_all(class_='pic')
#             for ul in film_url:
#                 urls = ul.find('a')['href']
#                 film_list_url.append(urls)
#             # print('电影链接：' + str(film_list_url))
#                 sheet.write_column('F2', film_list_url)
#
#             film_list_all.extend(film_list_number)
#             film_list_all.extend(film_list_name)
#             film_list_all.extend(film_list_grade)
#             film_list_all.extend(film_list_evaluation_number_people)
#             film_list_all.extend(film_list_quote)
#             film_list_all.extend(film_list_url)
#             # print(film_list_all)
#             # sheet.append(film_list_all)
#         for i in range(len(film_list_number)):
#             print('电影序号：' + film_list_number[i])
#             print('电影名：' + film_list_name[i])
#             print('电影评分：' + film_list_grade[i])
#             print('评价人数：' + film_list_evaluation_number_people[i])
#             print('推荐语：' + film_list_quote[i])
#             print('电影链接：' + film_list_url[i] + '\n')
#         wb.close()
#
#
# if __name__ == '__main__':
#     film()

# # 方法二：
# import bs4
# import openpyxl
# import requests
#
# x = 0
#
#
# def douban():
#     url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
#     # 0.模拟浏览器请求数据
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/87.0.4280.88 Safari/537.36 '
#     }
#     proxy = '39.104.68.232:8080'
#     # 需要认证的代理可以写成如下格式，username为用户名，password为密码
#     # proxy = "username:password@ip:端口号"
#     proxies = {
#         'http': 'https://' + proxy,
#     }
#     res = requests.get(url, proxies=proxies, headers=headers)
#     # 判断状态码是否正常
#     print(res.status_code)
#     bs = bs4.BeautifulSoup(res.text, 'html.parser')
#     bbs = bs.find('ol', class_="grid_view")
#
#     num_list = []
#     title_list = []
#     tes_list = []
#     comment_list = []
#     url_movie_list = []
#
#     # 创建Excel文件
#     wb = openpyxl.Workbook()
#     # 1获取工作簿
#     sheet = wb.active
#     sheet['A1'] = '豆瓣电影评分'
#     data = ['电影序号', '电影名', '电影评分', '推荐语', '电影链接']
#     # sheet.append('A1', ['电影序号', '电影名', '电影评分', '评价人数', '推荐语', '电影链接'])
#     sheet.append(data)
#     for titles in bbs.find_all('div', class_='item'):
#         # 查找序号
#         num = titles.find('em', class_="").text
#         num_list.append(num)
#         # 查找电影名
#         title = titles.find('span', class_="title").text
#         title_list.append(title)
#         # 查找推荐语
#         # tes = titles.find('span', class_="inq")
#         if not (titles.find('span', class_="inq")):
#             tes = '空'
#             tes_list.append(tes)
#         else:
#             tes = titles.find('span', class_="inq").text
#             tes_list.append(tes)
#         # 查找评分
#         comment = titles.find('span', class_="rating_num").text
#         comment_list.append(comment)
#         # 查找链接
#         url_movie = titles.find('a')['href']
#         url_movie_list.append(url_movie)
#
#         print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes + '\n' + url_movie)
#     sheet.append(num_list)
#     sheet.append(title_list)
#     sheet.append(comment_list)
#     sheet.append(tes_list)
#     sheet.append(url_movie_list)
#     wb.save('./douban_grade/电影评分.xlsx')
#
#
# for x in range(10):
#     douban()

import bs4
import xlsxwriter
from 使用IP代理模拟浏览器头 import reptile_header

film_list_all = []
# 查找序号
film_list_number = []
# 查找电影名
film_list_name = []
# 查找评分
film_list_grade = []
# 查找评价人数
film_list_evaluation_number_people = []
# 查找推荐语
film_list_quote = []
# 查找链接
film_list_url = []


def film_250(params):
    url = 'https://movie.douban.com/top250'
    douban_url = reptile_header(url=url, params=params)
    print(douban_url.status_code)
    bs = bs4.BeautifulSoup(douban_url.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")

    # 创建Excel文件
    wb = xlsxwriter.Workbook('./douban_grade/电影评分.xlsx')
    # 1获取工作簿
    sheet = wb.add_worksheet()
    # 写入表头
    sheet.write_row('A1', ['电影序号', '电影名', '电影评分', '评价人数', '推荐语', '电影链接'])

    for titles in bs.find_all('div', class_='item'):
        # 查找序号
        num = titles.find('em', class_="").text
        film_list_number.append(int(num))
        sheet.write_column('A2', film_list_number)
        # 查找电影名
        title = titles.find('span', class_="title").text
        film_list_name.append(title)
        sheet.write_column('B2', film_list_name)
        # 查找评分
        comment = titles.find('span', class_="rating_num").text
        film_list_grade.append(float(comment))
        sheet.write_column('C2', film_list_grade)
        # 评价人数
        number_peoples = titles.find('div', class_='star').text
        number_people = number_peoples.replace('\n', '')[3:]
        film_list_evaluation_number_people.append(int(number_people[:-3]))
        # film_list.append(film_evaluation_number_people.text.replace('\n', '')[3:])
        sheet.write_column('D2', film_list_evaluation_number_people)
        # 查找推荐语
        # tes = titles.find('span', class_="inq")
        if not (titles.find('span', class_="inq")):
            tes = '空'
            film_list_quote.append(tes)
            sheet.write_column('E2', film_list_quote)
        else:
            tes = titles.find('span', class_="inq").text
            film_list_quote.append(tes)
            sheet.write_column('E2', film_list_quote)
        # 查找链接
        url_movie = titles.find('a')['href']
        film_list_url.append(url_movie)
        sheet.write_column('F2', film_list_url)

        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes + '\n' + '评价人数：' + number_people + '\n' + url_movie)
    wb.close()


for p in range(10):
    params = {
            'start': (p * 25),
            'filter': ''
    }
    film_250(params)

# 从gevent库里导入monkey模块。
from gevent import monkey

# 把程序变成协作式运行，实现异步。
monkey.patch_all()

import requests
import time
import gevent
import csv
from bs4 import BeautifulSoup
from gevent.queue import Queue

start = time.time()


# 记录程序开始时间
# url_list = []


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


# 创建队列对象，并赋值给work。
work = Queue()

url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for num in range(1, 11):
    real_url = url_2.format(page=num)
    work.put_nowait(real_url)
    for page in range(1, 11):
        real_url = url_1.format(type=num, page=page)
        # 用put_nowait()函数可以把网址都放进队列里。
        work.put_nowait(real_url)
print(work)


# 当队列不是空的时候，就执行下面的程序。
def crawler():
    while not work.empty():
        # 用get_nowait()函数可以把队列里的网址都取出。
        food_url = work.get_nowait()
        # 用requests.get()函数抓取网址。
        res = header(url=food_url)
        time.sleep(0.3)
        # 打印网址、队列长度、抓取请求的状态码。
        print('*******************************************************')
        print(food_url, work.qsize(), res.status_code)
        print('*******************************************************')
        # 用requests.get获取网页源代码。
        bs_res = BeautifulSoup(res.text, 'html.parser')
        # 用BeautifulSoup解析网页源代码。
        group = bs_res.find_all(class_='text-box pull-left')
        for item in group:
            # 食物名称
            food_name = item.find('a')['title']
            # 食物热量详情
            food_data = item.find('a')['href']
            food_data_details = 'http://www.boohee.com' + food_data
            # 热量
            heat = item.find('p').text
            print(
                '--------------------------------------------------------------------------------------------------------------------------')
            print('食物名称：' + food_name + '\n热量： ' + heat + '\n食物热量详情页：' + food_data_details)
            write.writerow([food_name, heat, food_data_details])
    else:
        print('没有可执行的任务了！')


csv_file = open('boohee.csv', 'w', newline='', encoding='utf-8')
write = csv.writer(csv_file)
write.writerow(['食物名称', '热量', '食物热量详情页'])
# 创建空的任务列表
tasks_list = []
# 相当于创建了2个爬虫
for x in range(8):
    # 用gevent.spawn()函数创建执行crawler()函数的任务。
    task = gevent.spawn(crawler)
    # 往任务列表添加任务。
    tasks_list.append(task)

# 用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站。
gevent.joinall(tasks_list)
# 结束时间
end = time.time()
print(end - start)
csv_file.close()

# res = header(url=url)
# res.encoding = 'utf-8'
# soup = BeautifulSoup(res.text, 'html.parser')
# # print(res.status_code)
# group = soup.find_all(class_='text-box pull-left')
# for item in group:
#     # 食物名称
#     food_name = item.find('a')['title']
#     # 食物热量详情
#     food_data_details = item.find('a')['href']
#     # 热量
#     heat = item.find('p').text
#     print('--------------------------------------------------------------------------------------------------------------------------')
#     print('食物名称：' + food_name + '\n热量： ' + heat + '\n食物热量详情：http://www.boohee.com' + food_data_details)

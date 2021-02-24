# import os
# import cv2
# import numpy as np
# from PIL import Image
import csv
import time
import requests
from bs4 import BeautifulSoup

image_url_list = []
path = './amazon/images/'


# 头部信息
def header(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36'}
    # 设置代理IP
    proxy = '150.138.253.72:808'
    proxies = {
        'https': 'https://' + proxy,
    }
    res = requests.get(url=url, proxies=proxies, headers=headers)
    return res


url = 'http://m.cifnews.com/article/57739'
# 用requests.get()函数抓取网址。
res = header(url=url)
# 请求之后暂停一秒等网页数据
time.sleep(1)
print(res.status_code)
res.encoding = 'utf-8'
# 用requests.get获取网页源代码。
bs = BeautifulSoup(res.text, 'html.parser')
# 用BeautifulSoup解析网页源代码。
datas = bs.find_all(class_='cif-left')
# print(datas)
# 先将文章内容写进csv文件中
with open('./amazon/content.csv', 'w', newline='', encoding='utf-8')as file:
    write = csv.writer(file)
    for item in datas:
        # 标题
        article_title = item.find(class_='article-title').text
        print('标题：' + article_title)
        # 作者
        article_author = item.find(class_='introduce-name').text
        print('作者：' + article_author)
        # 文章简介
        article_summary = item.find(class_='article-summary').text
        print('文章简介：' + article_summary)
        # 文章内容
        article_content = item.find(class_='article-content').text.replace(' ', '')[:-146]
        print('文章内容：' + article_content)
        write.writerow(['标题：', article_title])
        write.writerow(['作者：', article_author])
        write.writerow(['文章简介：', article_summary])
        write.writerow(['文章内容：', article_content])

        # 文章中的图片链接
        content_url = item.find_all(class_='article-content')
        for p in content_url:
            images = p.find_all('img')
            for img in images:
                image = img['data-src']
                image_url_list.append(image)
print(image_url_list)

# 定义变量x并初始化用来计数图片的张数
x = 0
print('***************************')
for x in range(len(image_url_list)):
    # 获取获得的从imglist中遍历得到的imgurl
    re = requests.get(image_url_list[x])
    # print(re.status_code)
    imgres = re.content
    with open(path + '{}.jpg'.format(x + 1), 'wb') as f:
        f.write(imgres)
        x += 1
        print('正在下载，第', x, '张图片')
print('图片下载完毕')

# file_list = os.listdir(path)
# for file_name in file_list:
#     # 拼接文件路径
#     file_path = path + file_name
#     new_path = path + 'new_' + file_name
#     print('正在处理：' + file_name)
#
#     img = cv2.imread(file_path, 1)
#     hight, width, depth = img.shape[0:3]
#
#     # 截取
#     cropped = img[int(hight * 0.85):hight, int(width * 0.75):width]  # 裁剪坐标为[y0:y1, x0:x1]
#     cv2.imwrite(new_path, cropped)
#     imgSY = cv2.imread(new_path, 1)
#
#     # 图片二值化处理，把[200,200,200]-[250,250,250]以外的颜色变成0
#     thresh = cv2.inRange(imgSY, np.array([200, 200, 200]), np.array([250, 250, 250]))
#     # 创建形状和尺寸的结构元素
#     kernel = np.ones((3, 3), np.uint8)
#     # 扩展待修复区域
#     hi_mask = cv2.dilate(thresh, kernel, iterations=10)
#     specular = cv2.inpaint(imgSY, hi_mask, 5, flags=cv2.INPAINT_TELEA)
#     cv2.imwrite(new_path, specular)
#
#     # 覆盖图片
#     imgSY = Image.open(new_path)
#     img = Image.open(file_path)
#     img.paste(imgSY, (int(width * 0.75), int(hight * 0.85), width, hight))
#     img.save(new_path)

"""
前期准备工作：
1.下载并安装Python
2.下载并安装pip
3.使用pip命令安装所需要用到的模块（主要需要安装2个模块）
you-get模块、requests模块，安装命令如下（在命令行窗口输入）
pip install you-get
pip install requests
下载速度慢的化可以使用清华镜像
"""
import os
import requests


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
    # stream=True 使用视频流的方式下载视频
    res = requests.get(url=url, proxies=proxies, headers=headers, stream=True)
    return res


# 这是你需要下载视频的路径
url = 'https://www.bilibili.com/video/BV1J541187GA'
# 视频保存路径
video = r'D:\pythonProject\soup\下载视频\如何准备面试'
# 用requests.get()函数抓取网址。
res = header(url=url)
if res.status_code == 200:
    print('网站连接正常，准备下载...')
print('视频下载开始！')

try:
    os.system("you-get -o " + video + " " + url)  # 下载地址
    print("下载成功")
except:
    print("下载失败")


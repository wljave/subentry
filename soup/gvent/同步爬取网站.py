import requests
import time

# 程序运行后，你会看到同步的爬虫方式，是依次爬取网站，并等待服务器响应（状态码为200表示正常响应）后，才爬取下一个网站。
# 比如第一个先爬取了百度的网址，等服务器响应后，再去爬取新浪的网址，以此类推，直至全部爬取完毕。

# 导入requests和time
start = time.time()
# 记录程序开始时间

url_list = ['https://www.baidu.com/',
            'https://www.sina.com.cn/',
            'http://www.sohu.com/',
            'https://www.qq.com/',
            'https://www.163.com/',
            'http://www.iqiyi.com/',
            'https://www.tmall.com/',
            'http://www.ifeng.com/']
# 把8个网站封装成列表

for url in url_list:
    # 遍历url_list
    r = requests.get(url)
    # 用requests.get()函数爬取网站
    print(url, r.status_code)
    # 打印网址和抓取请求的状态码

end = time.time()
# 记录程序结束时间
print(end - start)
# end-start是结束时间减去开始时间，就是最终所花时间。
# 最后，把时间打印出来。

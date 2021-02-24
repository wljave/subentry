import requests
from bs4 import BeautifulSoup


# 发送请求
def get_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36 '
    }
    proxies = {'http': 'http://174.71.185.203:48678'}
    # 0.模拟浏览器请求数据
    response = requests.get(url=url, proxies=proxies, headers=headers)
    response.encoding = "utf8"
    # 判断状态码是否正常
    print(response.status_code)
    return response.text


# # 将数据写入文件
# def write_data():
#     for i in range(100):
#         url = "http://www.nimadaili.com/" + str(i+1)
#         data = get_data(url)
#         file = open('Proxies.txt', 'a+')
#         file.write(str(data))
#         file.close()
#
#
# # 验证该代理能否使用
# def verify(proxies):
#     req = requests.get("https://www.baidu.com", proxies=proxies)
#     return req.status_code


# 解析页面
def get_data(url):
    data = list()
    # 1.以网页源代码的格式获取数据
    html = get_info(url)
    # 2.以HTML解析数据
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("table", class_="table table-bordered table-hover small")
    soup = BeautifulSoup(str(table[0]), "lxml")
    trs = soup.find_all("tr")
    del trs[0]
    for tr in trs:
        ip = tr.select("td")[1].get_text()
        port = tr.select("td")[2].get_text()
        protocol = tr.select("td")[5].get_text()
        address = protocol.lower()+"://"+ip+":"+port
        proxies = {'http': address}
        if verify(proxies) == 200:
            data.append(address)
            return data


# if __name__ == '__main__':
#     write_data()

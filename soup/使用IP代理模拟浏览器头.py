import requests


def reptile_header(url, params):
    global res
    # 模拟浏览器请求数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36 ',
        # 爬取QQ音乐里面的歌词信息的时候，如果不添加origin和referer就会读取不到数据【{'retcode': -1310, 'code': -1310, 'subcode': -1310}】
        # 'origin': 'https://y.qq.com',
        # 'referer': 'https://y.qq.com/'
        # 查询快递使用
        # 'Host': 'www.kuaidi100.com',
        # 'Referer': 'https://www.kuaidi100.com/'
    }
    # 设置代理IP
    proxy = '171.97.15.9:8080'
    # 需要认证的代理可以写成如下格式，username为用户名，password为密码
    # proxy = "username:password@ip:端口号"
    proxies = {
        'http': 'https://' + proxy,
    }
    res = requests.get(url=url, params=params, proxies=proxies, headers=headers)
    # 判断状态码是否正常
    # print(res.status_code)
    return res

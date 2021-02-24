import requests
from bs4 import BeautifulSoup

# 歌手的音乐信息
song_keyword_name = input('请输入您搜索的歌手名字：')
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):

    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '70717568573156220',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': song_keyword_name,
        'g_tk': '714057807',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    # 将参数封装为字典
    res_music = requests.get(url, params=params)
    # 调用get方法，下载这个列表
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
        # list_music是一个列表，music是它里面的元素
        print(music['name'])
        # 以name为键，查找歌曲名
        print('所属专辑：' + music['album']['name'])
        # 查找专辑名
        print('播放时长：' + str(music['interval']) + '秒')
        # 查找播放时长
        print('播放链接：https://y.qq.com/n/yqq/song/' + music['mid'] + '.html\n\n')
        # 查找播放链接

# 歌词
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

headers = {
    'origin': 'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
}
# 伪装请求头

# 设置代理IP
proxy = '5.196.23.219:80'
# 需要认证的代理可以写成如下格式，username为用户名，password为密码
# proxy = "username:password@ip:端口号"
proxies = {
    'http': 'https://' + proxy,
}

for i in range(5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': i + 1,
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    # 将参数封装为字典
    res_music = requests.get(url, headers=headers, proxies=proxies, params=params)
    # 发起请求，填入请求头和参数

    print('第%d个请求状态为：' % (i + 1) + str(res_music.status_code))
    lyric = res_music.json()
    # 一层一层地取字典，获取歌单列表
    list_music = lyric['data']['song']['list']
    # list_music是一个列表，music是它里面的元素

    # 获得歌词id，为爬取歌词最准备
    list_music_lyric_ids = []
    list_music_name = []

    for music in list_music:
        # 获得歌词id，为爬取歌词最准备
        music_lyric_id = music['id']
        list_music_lyric_ids.append(music_lyric_id)

        # 获得歌曲名,以name为键
        music_name = music['name']
        list_music_name.append(music_name)


    # 爬取歌词
    def lyric(par):
        lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'

        # 调用get方法，下载这个字典
        res_lyric = requests.get(url=lyric_url, headers=headers, proxies=proxies, params=par)
        res_lyric.encoding = 'utf-8'
        # print('第二个请求状态为：'+str(res_lyric.status_code))

        # 爬取歌词json字典
        music_lyric = res_lyric.json()
        # print(music_lyric)
        try:
            lyrics = music_lyric['lyric']
            soup = BeautifulSoup(lyrics, 'html.parser')
            print(soup)
            # print(lyrics)
        except KeyError:
            print('歌曲  ┝ 暂无歌词')


    # 根据歌词id查找对应的歌词
    k = 0
    while k < 20:
        for ids in list_music_lyric_ids:
            par = {
                'nobase64': '1',
                'musicid': ids,
                '-': 'jsonp1',
                'g_tk_new_20200303': '',
                'g_tk': '',
                'loginUin': '0',
                'hostUin': '0',
                'format': 'json',
                'inCharset': 'utf8',
                'outCharset': 'utf-8',
                'notice': '0',
                'platform': 'yqq.json',
                'needNewCode': '0'
            }
            k += 1
            print('第%d首' % k)
            lyric(par)

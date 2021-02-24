# 用来读写Excel
# import openpyxl
# 爬取HTML网页(第一个请求Doc)
# from bs4 import BeautifulSoup
# 用来对字符串进行转码操作
# from urllib.request import quote
# 将openpyxl定义的非法字符用空字符代替
import xlsxwriter
from 使用IP代理模拟浏览器头 import reptile_header

song_keyword_name = input('请输入您搜索的歌手名字：')
# film_name = quote(song_keyword_name.encode('utf-8'))

search_url = 'https://y.qq.com/portal/search.html'
params = {
    'page': '1',
    'searchid': '1',
    'remoteplace': 'txt.yqq.top',
    't': 'song',
    'w': song_keyword_name
}
res_song_name_url = reptile_header(url=search_url, params=params)
print('歌手【%s】详情信息链接：%s' % (song_keyword_name, res_song_name_url.url))

# 创建Excel文件
wb = xlsxwriter.Workbook('./crawl_song/%s-歌曲详细信息.xlsx' % song_keyword_name)
# 获取工作簿的活动表
# sheet = wb.worksheets()
# 创建工作表
sheet = wb.add_worksheet(song_keyword_name)
# 添加工作表样式
bold = wb.add_format({
        'bold':  True,  # 字体加粗
        'border': 1,  # 单元格边框宽度
        'align': 'left',  # 水平对齐方式
        'valign': 'vcenter',  # 垂直对齐方式
        'fg_color': '#819FF7',  # 单元格背景颜色
        'text_wrap': True,  # 是否自动换行
    })

# 加表头，给单元格赋值
# sheet['A1'] = '歌曲ID'
# sheet['B1'] = '歌曲名'
# sheet['C1'] = '选自'
# sheet['D1'] = '歌手'
# sheet['E1'] = '所属专辑'
# sheet['F1'] = '出版时间'
# sheet['G1'] = '播放时长'
# sheet['H1'] = '播放链接'
# sheet.append(['歌曲ID', '歌曲名', '选自', '歌手', '所属专辑', '出版时间', '播放时长', '播放链接'])
# 写入一整行 row:行， col：列， data:要写入的数据, bold:单元格的样式
sheet.write_row('A1', ['歌曲ID', '歌曲名', '选自', '歌手', '所属专辑', '出版时间', '播放时长', '播放链接'], bold)


# list_music_lyric_ids = []
music_name = ''
sub_code = ''
singer = ''
# singers_name = []
key = True
i = 1
j = 0


def song_message(param):
    global music_name, i, j, sub_code, singer
    xhr = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    # 调用get方法，下载这个字典
    res_music_message = reptile_header(url=xhr, params=param)
    res_music_message.encoding = 'utf-8'
    if res_music_message.status_code == 200:
        print('连接正常，可以正常爬取')
    # 使用json()方法，将response对象，转为列表/字典
    json_music = res_music_message.json()
    # 一层一层地取字典，获取歌单列表
    list_music = json_music['data']['song']['list']
    # 根据subcode判断歌曲是否存在
    sub_code = json_music['subcode']

    for music in list_music:
        # 获得歌词id，为爬取歌词最准备
        music_lyric_id = music['id']
        # list_music_lyric_ids.append(music_lyric_id)
        # 以name为键，查找歌曲名
        music_name = music['name']
        # 歌曲名称副标题-出自
        come_from = music['lyric']
        # 取出歌手作者名字
        singer_name = music['singer']
        for song in singer_name:
            singer = song['name']
            # singers_name.append(singer)
            # sheet.write_column('I2', singers_name)
            print('歌曲《' + music_name + '》的' + '歌唱者是：' + singer)

        # 发布时间
        release_time = music['time_public']
        # 查找所属专辑名
        album = music['album']['name']
        # 查找播放时长----判断时长是否为0，判断歌曲是否因版权已经下架
        running_time = music['interval']
        # 查找播放链接
        song_play_url = 'https://y.qq.com/n/yqq/song/' + music['mid'] + '.html'
        # 歌曲ID+歌曲名+选自+歌手+所属专辑+出版时间+播放时长+播放链接
        # sheet.append([music_lyric_id, music_name, come_from, singer, album, release_time, running_time, song_play_url])
        data = [music_lyric_id, music_name, come_from, singer, album, release_time, running_time, song_play_url]
        # 写入一整行
        sheet.write_row('A%d' % (j+2), data)
        print('第%d条下载成功' % (j+1))
        j += 1
    # print('第%d页保存完毕\n' % i)
    i += 1
    # wb.save('./crawl_song/%s-歌曲详细信息.xlsx' % song_keyword_name)


p = 1
while key:
    # 每页显示的数量最大显示60条
    param = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '67751296646578192',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': p,
        'n': '60',
        'w': song_keyword_name,
        'g_tk_new_20200303': '1464878100',
        'g_tk': '1592435056',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    p += 1
    song_message(param)
    # print("%s-歌曲详细信息.xlsx文件保存成功，处理结束！" % song_keyword_name)
    if sub_code != 0:
        key = False
        print('歌曲信息到此结束了！')
        print("%s-歌曲详细信息.xlsx文件保存成功，处理结束！" % song_keyword_name)
        wb.close()
#
# # 爬取歌词
# def lyric(par):
#     lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
#
#     # 调用get方法，下载这个字典
#     res_lyric = reptile_header(url=lyric_url, params=par)
#     res_lyric.encoding = 'utf-8'
#     if res_lyric.status_code == 200:
#         print('连接正常，可以正常爬取\n')
#
#     # # 1以网页源代码的格式获取数据
#     # html = res_lyric.text
#     # # 2解析数据
#     # soup = BeautifulSoup(html, 'html.parser')
#     # 找到歌词位置，并复制给music_lyric
#     music_lyric = res_lyric.json()
#     print(music_lyric['lyric'])
#
#
# k = 0
# while k < 60:
#     for ids in list_music_lyric_ids:
#         par = {
#             'nobase64': '1',
#             'musicid': ids,
#             '-': 'jsonp1',
#             'g_tk_new_20200303': '1464878100',
#             'g_tk': '1592435056',
#             'loginUin': '0',
#             'hostUin': '0',
#             'format': 'json',
#             'inCharset': 'utf8',
#             'outCharset': 'utf-8',
#             'notice': '0',
#             'platform': 'yqq.json',
#             'needNewCode': '0'
#         }
#         k += 1
#         lyric(par)


# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6'
# # 模拟浏览器请求数据
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/87.0.4280.88 Safari/537.36 '
# }
# # 设置代理IP
# proxy = '103.109.59.242:53281'
# # 需要认证的代理可以写成如下格式，username为用户名，password为密码
# # proxy = "username:password@ip:端口号"
# proxies = {
#     'http': 'https://' + proxy,
# }
# res_music = requests.get(url, proxies=proxies, headers=headers)
# # 判断状态码是否正常
# print(res_music.status_code)
#
# # 1以网页源代码的格式获取数据
# html = res_music.text
# # 2解析数据
# # 请求html，得到response
# bs_music = BeautifulSoup(html, 'html.parser')
# # ##因为bs_music里面没有我们要的数据，所以下面会得到一个空[]#################################################
# # #######想要的数据在XHR中的JSON文件中########
# # print(bs_music)
# # 解析html
# list_music = bs_music.find_all('a', class_='js_song')
# # 查找class属性值为“js_song”的a标签，得到一个由标签组成的列表
# for music in list_music:
#     # 对查找的结果执行循环
#     print(music['title'])
#     # 打印出我们想要的音乐名
#
# # 直接引入XHR的JSON链接
# xhr = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=64704850617205118&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
# # 调用get方法，下载这个字典
# res_music = requests.get(xhr)
# # 使用json()方法，将response对象，转为列表/字典
# json_music = res_music.json()
# # 一层一层地取字典，获取歌单列表
# list_music = json_music['data']['song']['list']
# # list_music是一个列表，music是它里面的元素
# for music in list_music:
#     # 以name为键，查找歌曲名
#     print('歌曲名称：' + music['name'])
#     # 查找专辑名
#     print('所属专辑：' + music['album']['name'])
#     # 查找播放时长
#     print('播放时长：' + str(music['interval']) + '秒')
#     # 查找播放链接
#     print('播放链接：https://y.qq.com/n/yqq/song/' + music['mid'] + '.html\n\n')

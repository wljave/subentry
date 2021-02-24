import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 ',
    'Referer': 'http://103.242.175.216:197/nlpir/',
}
# 设置代理IP
proxy = '39.106.223.134:80'
proxies = {'http': 'http://' + proxy}

# words = input('你想翻译的是什么呀？\n')
url = 'http://103.242.175.216:197/nlpir/index6/getWord2Vec.do'
keywords = input('请输入你要联想的词汇：')
data = {
    'content': keywords,
}

res = requests.post(url=url, headers=headers, proxies=proxies, data=data)
res.encoding = 'utf-8'
print(res.status_code)
# 使用dumps()函数，将列表a转换为json格式的字符串，赋值给b。
answer = json.loads(res.text)
# print(answer)
# print(type(answer))
for i in answer['w2vlist']:
    beat = i.split(',')
    print(beat[0])

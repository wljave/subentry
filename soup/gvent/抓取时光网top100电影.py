import requests
import csv

url = 'http://front-gateway.mtime.com/library/index/app/topList.api?tt='
res = requests.get(url)
print(res.status_code)
res.encoding = 'utf-8'
movieTopList = res.json()
print(type(movieTopList))

with open('movieTV.csv', 'w', newline='', encoding='utf-8')as f:
    write = csv.writer(f)
    write.writerow(['编号', '影片名', '导演名', '主演名', '主要奖项', '评分', '发行时间', '发行国家地区', '详情页'])

    # 只需要找到‘时光电影’【movieTopList['data']['movieTopList']['topListInfos'][0]['items']】
    movie = movieTopList['data']['tvTopList']['topListInfos'][0]['items']
    for item in movie:
        # 电影编号
        rank = item['rank']
        # 电影ID
        movieId = item['itemId']
        # 电影影片名
        movieName = item['movieInfo']['movieName']
        # 电影导演名
        director = item['movieInfo']['director']
        if not director:
            director = ''
        # 电影主演名
        actors = item['movieInfo']['actors']
        if not actors:
            actors = ''
        # 电影主要奖项
        award = item['movieInfo']['award']
        if not award:
            award = ''
        # 电影发行时间
        releaseDate = item['movieInfo']['releaseDate']
        # 电影发行国家地区
        releaseLocation = item['movieInfo']['releaseLocation']
        if not releaseLocation:
            releaseLocation = ''
        # 电影评分
        score = item['movieInfo']['score']
        write.writerow([str(rank), movieName, director, actors, award, score, releaseDate, releaseLocation, 'http://movie.mtime.com/' + movieId])
        print('--------------------------------------------------------------------')
        print('编号:' + str(rank))
        # print('电影ID:' + movieId)
        print('影片名:' + movieName)
        print('导演名:' + director)
        print('主演名:' + actors)
        print('主要奖项:' + award)
        print('评分:' + score)
        print('发行时间:' + releaseDate)
        print('发行国家地区:' + releaseLocation)
        print('详情页:' + 'http://movie.mtime.com/' + movieId)

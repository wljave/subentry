import scrapy
import bs4
from ..items import DoubanItem
# 需要引用DoubanItem，它在items里面。
# 因为是items在top250.py的上一级目录，所以要用..items，这是一个固定用法。


# 定义一个爬虫类DoubanSpider。
class DoubanSpider(scrapy.Spider):
    # 定义爬虫的名字为douban。
    name = 'douban'
    # 定义爬虫爬取网址的域名。
    allowed_domains = ['book.douban.com']
    # 定义起始网址。
    start_urls = []
    for x in range(3):
        books_url = 'https://book.douban.com/top250?start=' + str(x*25)
        # 把豆瓣Top250图书的前10页网址添加进start_urls。
        start_urls.append(books_url)

    # parse是默认处理response的方法。
    def parse(self, response, **kwargs):
        # print(response.text)
        # 用BeautifulSoup解析response。
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        # 用find_all提取<tr class="item">元素，这个元素里含有书籍信息。
        datas = bs.find_all('tr', claas_='item')
        # 遍历data
        for data in datas:
            # 实例化DoubanItem这个类。
            item = DoubanItem()

            # item['title'] = data.find_all('a')[1]['title']
            # # 提取出书名，并把这个数据放回DoubanItem类的title属性里。
            # item['publish'] = data.find('p', class_='pl').text
            # # 提取出出版信息，并把这个数据放回DoubanItem类的publish里。
            # item['score'] = data.find('span', class_='rating_nums').text

            # 图书封面图片链接
            item['imges'] = data.find('img')['src']
            # 书名
            item['title'] = data.find_all(class_='pl2').find('a')['title']
            # 该书的详情页链接
            item['particulars'] = data.find_all(class_='pl2').find('a')['href']
            # 图书的出版信息
            item['publisher'] = data.find('p', class_='pl').text
            # 图书的评分及评价人数
            item['grade'] = data.find(class_='star clearfix').text
            # 图书简评
            item['brief_comment'] = data.find('p', class_='quote').text
            # 打印上述信息。
            print(item['title'])
            # yield item是把获得的item传递给引擎。
            yield item

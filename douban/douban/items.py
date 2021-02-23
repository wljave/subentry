# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # # 定义一个类DoubanItem，它继承自scrapy.Item
    # title = scrapy.Field()
    # # 定义书名的数据属性
    # publish = scrapy.Field()
    # # 定义出版信息的数据属性
    # score = scrapy.Field()
    # # 定义评分的数据属性

    # 图书封面图片链接
    imges = scrapy.Field()
    # 书名
    title = scrapy.Field()
    # 该书的详情页链接
    particulars = scrapy.Field()
    # 图书的出版信息
    publisher = scrapy.Field()
    # 图书的评分及评价人数
    grade = scrapy.Field()
    # 图书简评
    brief_comment = scrapy.Field()

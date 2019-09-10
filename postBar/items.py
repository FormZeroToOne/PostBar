# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostbarItem(scrapy.Item):

    url = scrapy.Field()  # 贴吧链接
    title = scrapy.Field()  # 标题
    author = scrapy.Field()  # 作者
    nums = scrapy.Field()  # 贴吧回帖数
    connect = scrapy.Field()  # 贴吧内容

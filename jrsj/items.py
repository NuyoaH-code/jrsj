# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#存放爬虫爬取下来数据的模型
import scrapy


class JrsjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    cont=scrapy.Field()
    url=scrapy.Field()
    source_name=scrapy.Field()
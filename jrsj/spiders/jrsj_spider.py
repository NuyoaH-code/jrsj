# -*- coding: utf-8 -*-
import time
import random
import scrapy
from jrsj.items import JrsjItem
from scrapy import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class JrsjSpiderSpider(scrapy.Spider):
    name = 'jrsj_spider'
    allowed_domains = ['finance.591hx.com']   #过滤爬取的域名
    start_urls = ['http://finance.591hx.com/lista/jrsctj.shtml']

    def parse(self, response):   #parse函数会被当做一个生成器使用
        #response可以执行xpath和css来提取数据
        xinwenlis=response.xpath("//div[@id='content']/div[@id='main']//ul/li")
        for xinwenli in xinwenlis:
            #item放在循环体里面
            item=JrsjItem()
            url=xinwenli.xpath(".//a/@href").getall()
            if url:
                item['url']="".join(url).strip()
                yield scrapy.Request(item['url'],meta={'item':item},callback=self.detail)
            #翻页操作
            next_url=response.xpath("//div[@class='page']/a[3]/@href").get()
            if not next_url:
                return
            else:
                yield scrapy.Request(next_url,callback=self.parse)
    def detail(self,response):
        #接收上级已爬取的数据
        print("===已经进入内页===")
        item=response.meta['item']
        #一级内页数据提取
        title=response.xpath("//div[@class='news bc mt12']/h1/text()").getall()
        item['title']="".join(title).strip()
        source_name=response.xpath("//div[@class='info']/text()").getall()
        item['source_name']="".join(source_name).strip()
        try:
            cont=response.xpath("//div[@class='newsContainer']/p/text()").getall()
            item['cont']="".join(cont).strip()
        except:
            cont=response.xpath("//div[@class='newsContainer']/text()").getall()
            item['cont']="".join(cont).strip()

        yield item
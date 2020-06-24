# -*- coding: utf-8 -*-
#用来将items的模型存储到本地磁盘中
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# class JrsjPipeline:
#     def __init__(self):
#         self.fp=open("xinwenli.json",'w',encoding='utf-8')
#     def open_spider(self,spider):
#         print('爬虫开始了...')
#     def process_item(self, item, spider):
#         #将item转换为字典
#         item_json=json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
#     def close_spider(self,spider):
#         self.fp.close()
#         print('爬虫结束了')

# from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter
# class JrsjPipeline:
#     def __init__(self):
#         #wb以二进制方式打开
#         self.fp=open("xinwenli.json",'wb')
#         self.exporter=JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#     def open_spider(self,spider):
#         print('爬虫开始了...')
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('爬虫结束了')

from scrapy.exporters import JsonLinesItemExporter
class JrsjPipeline:
    def __init__(self):
        #wb以二进制方式打开
        self.fp=open("xinwenli.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print('爬虫开始了...')
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def close_spider(self,spider):
        self.fp.close()
        print('爬虫结束了')
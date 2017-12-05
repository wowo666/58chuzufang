# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo,json


class ChuzufangPipeline(object):

    def __init__(self):
        self.file = open('chuzu.json','wb')

    def process_item(self, item, spider):
        str_data = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(str_data.encode())
        return item

    def __del__(self):
        self.file.close()

class MongoPipeline(object):
    def __init__(self):
        # 获取setting主机名、端口号和数据库名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        # 创建MongoDB链接
        self.client = pymongo.MongoClient(host=host, port=port)
        # 指定的数据库
        self.mdb = self.client[dbname]
        # 获取数据库里存放数据的表名
        self.table = self.mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)
        self.table.insert(data)
        return item

    def __del__(self):
        self.client.close()

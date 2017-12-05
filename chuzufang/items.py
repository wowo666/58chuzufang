# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChuzufangItem(scrapy.Item):
    # define the fields for your item here like:
    # 简介
    house_title = scrapy.Field()
    # 详情链接
    link = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 租赁方式
    lease = scrapy.Field()
    # 房屋类型
    type = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 房屋楼层
    floor = scrapy.Field()
    # 小区
    estate = scrapy.Field()
    # 地址
    addr = scrapy.Field()
    # 联系电话
    tel = scrapy.Field()
    # 装修情况
    decoratiom = scrapy.Field()
    # 描述
    desc = scrapy.Field()
    # 发布时间
    pubdate = scrapy.Field()
    # 房源详情
    source = scrapy.Field()
    pass

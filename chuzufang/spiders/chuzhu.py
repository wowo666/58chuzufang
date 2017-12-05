# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from chuzufang.items import ChuzufangItem


class ChuzhuSpider(CrawlSpider):
    name = 'chuzhu'
    allowed_domains = ['58.com']
    start_urls = ['http://sh.58.com/chuzu/']

    rules = (
        # 详情页链接
        Rule(LinkExtractor(allow=r'/zufang/\d+?x.shtml'), callback='parse_item'),
        # 翻页链接
        Rule(LinkExtractor(allow=r'/chuzu/pn\d+/$'),follow=True),
    )

    def parse_item(self, response):
        # print(response.url,"++++++++")
        item = ChuzufangItem()
        house_title = response.xpath('//div[@class="house-title"]/h1/text()').extract_first()
        if house_title:
            item['house_title'] = house_title
            item['link'] = response.url
            item['price'] = response.xpath('//div[@class="house-pay-way f16"]/span/b/text()').extract_first() + '元/月'
            item['lease'] = response.xpath('//ul[@class="f14"]/li[1]/span[2]/text()').extract_first()
            type_list = response.xpath('//ul[@class="f14"]/li[2]/span[2]/text()').extract_first().split(' ')

            temp = []
            for val in type_list:
                if val != '':
                    temp.append(val)
            item['area'] = temp[1].replace('\xa0\xa0','') + '平'
            item['type'] = temp[0]
            item['decoratiom'] = temp[2].replace('平\xa0\xa0','')
            item['estate'] = response.xpath('//ul[@class="f14"]/li[4]/span[2]/a/text()').extract_first()
            item['addr'] = response.xpath('//ul[@class="f14"]/li[6]/span[2]/text()').extract_first().replace('\r\n','').strip()
            item['tel'] = response.xpath('//div[@class="house-chat-phone"]/span/text()').extract_first()
            item['source'] = response.xpath('//ul[@class="house-disposal"]/li/text()').extract()
            item['desc'] = ''.join(response.xpath('//span[@class="a2"]/p/span/text()').extract()).replace('\t','').replace('\xb2','').replace('\xa0','')
            # item['pubdate'] = response.xpath().extract_first()
            print(item)
            yield item

# -*- coding: utf-8 -*-
import scrapy
from project.items import ProjectItem

class PneumoniaSpider(scrapy.Spider):
    name = 'pneumonia'
    allowed_domains = ['123.sogou.com/zhuanti/pneumonia.html?fr=sgnews']
    start_urls = ['http://123.sogou.com/zhuanti/pneumonia.html?fr=sgnews/']

    def parse(self, response):
        item = ProjectItem()
        item['Confirmed'] = response.xpath('/html/body/section[1]/div/div[1]/div[1]/text()').extract_first()
        item['Suspected'] = response.xpath('/html/body/section[1]/div/div[2]/div[1]/text()').extract_first()
        item['Healing'] = response.xpath('/html/body/section[1]/div/div[3]/div[1]/text()').extract_first()
        item['Death'] = response.xpath('/html/body/section[1]/div/div[4]/div[1]/text()').extract_first()
        item['Deadline'] = response.xpath('/html/body/section[1]/p[1]/text()').extract_first()[3:]
        yield item
'''

'''
# -*- coding: utf-8 -*-
import scrapy
from project.items import Pro_ProjectItem

class ProPneumoniaSpider(scrapy.Spider):
    name = 'pro_pneumonia'
    allowed_domains = ['123.sogou.com/zhuanti/pneumonia.html?fr=sgnews']
    start_urls = ['http://123.sogou.com/zhuanti/pneumonia.html?fr=sgnews/']

    def parse(self, response):
        obj_list = response.xpath('/html/body/section[3]/div/div')[1:-1]
        for obj in obj_list:
            item = Pro_ProjectItem()
            item['province_Name'] = obj.xpath('./div[1]/text()').extract_first()
            item['province_Confirmed'] = obj.xpath('./div[2]/text()').extract_first()
            item['province_Death'] = obj.xpath('./div[3]/text()').extract_first()
            if item['province_Death'] is None:
                item['province_Death'] = '无'
            item['province_Healing'] = obj.xpath('./div[4]/text()').extract_first()
            if item['province_Healing'] is None:
                item['province_Healing'] = '无'
            yield item

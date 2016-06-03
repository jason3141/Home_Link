# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Home_Link.items import HomeLinkItem


class HomeSpider(CrawlSpider):
	name = "home_link"
	allow_domains = ['nj.lianjia.com']
	start_urls = ['http://nj.lianjia.com/ershoufang/']
	rules = (
		Rule(LinkExtractor(allow=(r'\d+\.html', r'pg\d+\\')), callback='parse_item', follow=True),
	)
	
	def parse_item(self, response):
		l = ItemLoader(item=HomeLinkItem(), response=response) 
		l.add_xpath('id', '//div[@class="content"]/span[@class="sharethis"]/span[@class="erweibox"]/img') 
		l.add_value('url', response.url)
		l.add_xpath('title', '//title/text()')
		l.add_xpath('price', '//div[@class="content"]/div[@class="price "]/span[@class="total"]/text()')
		l.add_xpath('room', '//div[@class="content"]/div[@class="houseInfo"]/div[@class="room"]/div[@class="mainInfo"]/text()')
		l.add_xpath('type', '//div[@class="content"]/div[@class="houseInfo"]/div[@class="type"]/div[@class="mainInfo"]/text()')
		l.add_xpath('area', '//div[@class="content"]/div[@class="houseInfo"]/div[@class="area"]/div[@class="mainInfo"]/text()')
		l.add_xpath('areaName', '//div[@class="content"]/div[@class="aroundInfo"]/div[@class="communityName"]/a[@class="info"]/text()')
		return l.load_item()
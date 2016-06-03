# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


def filter_id(id):
    return id.split(' ')[1].split('=')[2].strip('"')


def encode_custom(value):
    return value.encode('utf-8')


class HomeLinkItem(scrapy.Item):
    id = scrapy.Field(
        input_processor=MapCompose(filter_id),
    )
    url = scrapy.Field()
    title = scrapy.Field(
        input_processor=MapCompose(encode_custom)
    )
    price = scrapy.Field()
    room = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    areaName = scrapy.Field()

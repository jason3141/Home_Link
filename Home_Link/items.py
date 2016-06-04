# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def filter_id(hid):
    return hid.split(' ')[1].split('=')[2].strip('"')


def filter_title(title):
    return title.split('_')[0]


class HomeLinkItem(scrapy.Item):
    hid = scrapy.Field(
        input_processor=MapCompose(filter_id),
        output_processor=TakeFirst()
    )
    url = scrapy.Field(
        output_processor=TakeFirst()
    )
    title = scrapy.Field(
        input_processor=MapCompose(filter_title),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        output_processor=TakeFirst()
    )
    room = scrapy.Field(
        output_processor=TakeFirst()
    )
    htype = scrapy.Field(
        output_processor=TakeFirst()
    )
    area = scrapy.Field(
        output_processor=TakeFirst()
    )
    areaName = scrapy.Field(
        output_processor=TakeFirst()
    )

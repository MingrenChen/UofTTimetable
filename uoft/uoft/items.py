# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UoftItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    name = scrapy.Field()
    lec = scrapy.Field()
    tut = scrapy.Field()
    lab = scrapy.Field()
    pre = scrapy.Field()
    exc = scrapy.Field()
    br = scrapy.Field()
    time = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FiltItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    from1=scrapy.Field()
    to=scrapy.Field()
    time=scrapy.Field()
    value=scrapy.Field()

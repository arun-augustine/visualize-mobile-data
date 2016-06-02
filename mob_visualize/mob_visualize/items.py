# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MobVisualizeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    lowest_price = scrapy.Field()
    launch_date = scrapy.Field()
    features = scrapy.Field()
    user_rating = scrapy.Field()
    review_count = scrapy.Field()

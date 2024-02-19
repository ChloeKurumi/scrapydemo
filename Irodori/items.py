# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 作者的英文
class AuthorItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    name = scrapy.Field()
    avatar = scrapy.Field()

#作品的英文
class ComicItem(scrapy.Item):
    # define the fields for your item here like:
    jp_title = scrapy.Field()
    artist = scrapy.Field()
    rm_title = scrapy.Field()
    title = scrapy.Field()
    pages = scrapy.Field()



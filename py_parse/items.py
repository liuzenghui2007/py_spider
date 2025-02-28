import scrapy

class ItcastItem(scrapy.Item):
   name = scrapy.Field()
   title = scrapy.Field()
   info = scrapy.Field()

class HypeAuditorItem(scrapy.Item):
    rank = scrapy.Field()
    nick = scrapy.Field()
    firstName = scrapy.Field()
    category = scrapy.Field()
    followers = scrapy.Field()
    country = scrapy.Field()
    engAuth = scrapy.Field()
    engAvg = scrapy.Field()

class HypeAuditorYouTubeCategoryItem(scrapy.Item):
    rank = scrapy.Field()
    contributorContentUsername=scrapy.Field()
    contributorContentFullname=scrapy.Field()
    category = scrapy.Field()
    followers = scrapy.Field()
    viewsAvg= scrapy.Field()
    likesAvg = scrapy.Field()
    commentsAvg = scrapy.Field()
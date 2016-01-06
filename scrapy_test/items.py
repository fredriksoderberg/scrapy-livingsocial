from scrapy.item import Item, Field

class LivingSocialDeal(Item):
    title = Field()
    link = Field()
    location = Field()
    original_price = Field()
    price = Field()
    end_date = Field()
    
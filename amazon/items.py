# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from itemloaders.processors import TakeFirst, Join, MapCompose
import scrapy
from w3lib.html import strip_html5_whitespace, remove_tags


def strip_amp(word):
    return word.replace("amp;", "")


class AmazonItem(scrapy.Item):
    Category = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst(),
    )
    Subcategory = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace, strip_amp),
        output_processor=Join(),
    )
    Brand = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst(),
    )
    Manufacturer_Part_Number = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst(),
    )

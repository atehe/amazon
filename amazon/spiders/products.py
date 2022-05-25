import scrapy
from itemloaders import ItemLoader
from amazon.items import AmazonItem


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["."]

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.amazon.com/dp/B0872DG7LD", callback=self.parse
        )

    def parse(self, response):
        loader = ItemLoader(item=AmazonItem(), selector=response)
        loader.add_xpath(
            "Category", "//select[@id='searchDropdownBox']/option[@selected='selected']"
        )
        loader.add_xpath(
            "Subcategory",
            "//ul[@class='a-unordered-list a-horizontal a-size-small']/li",
        )
        loader.add_xpath(
            "Brand",
            "//table[@id='productDetails_techSpec_section_1']//th[contains(text(), 'Brand')]/following-sibling::td",
        )
        loader.add_xpath(
            "Manufacturer_Part_Number",
            "//table[@id='productDetails_techSpec_section_1']//th[contains(text(), 'Part Number')]/following-sibling::td",
        )

        yield loader.load_item()

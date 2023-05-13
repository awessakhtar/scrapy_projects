import scrapy
from ..items import QuotestutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response, **kwargs):
        quote_block = response.css('div.quote')

        items = QuotestutorialItem()

        for quotes in quote_block:
            quote = quotes.css('.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['quote'] = quote 
            items['author'] = author 
            items['tag'] = tag

            yield items
        
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
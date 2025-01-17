import scrapy
from scrapy.crawler import CrawlerProcess

class WebScraper(scrapy.Spider):
    name = "scraper"
    start_urls = ["https://quotes.toscrape.com"]
    def parse(self, response):
        print("The content found is:")
        content = response.css('span.text::text')
        for count, quote in enumerate(content, 1):
            print(f"{count}. {quote.get()}")
output = CrawlerProcess()
output.crawl(WebScraper)
output.start()

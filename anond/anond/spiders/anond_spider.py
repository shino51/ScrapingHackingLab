import scrapy


class AnondSpiderSpider(scrapy.Spider):
    name = "anond_spider"
    allowed_domains = ["anond.hatelabo.jp"]
    start_urls = ["https://anond.hatelabo.jp"]

    def parse(self, response, **kwargs):
        for url in response.css('p.sectionfooter a::attr("href")'):
            yield response.follow(url)

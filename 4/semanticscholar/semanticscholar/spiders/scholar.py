from urllib.parse import urlencode
import scrapy


class HumanVerificationMiddleware:
    def process_request(self, request, response, spider):
        if response.xpath("//head/title/text()") == "Human Verification":
            # TODO: solve captcha here and return retry request
            pass
        return response


class ScholarSpider(scrapy.Spider):
    name = "papers"
    
    start_urls = [
        
    ]

    # TODO: Define item count limit, middlewares, feed exports, etc.
    custom_settings = {
        "ITEM_PIPELINES": {"semanticscholar.pipelines.SemanticscholarPipeline": 300},
        "DOWNLOADER_MIDDLEWARES": {
            "semanticscholar.middlewares.SemanticscholarDownloaderMiddleware": 543,
            "semanticscholar.spiders.scholar.HumanVerificationMiddleware": 600,
        },
        "FEEDS": {
            "../../../Kasaee.json": {"format": "json"},
            "../../../Rabiee.json": {"format": "json"},
            "../../../Rohban.json": {"format": "json"},
            "../../../Soleymani.json": {"format": "json"},
        },
        "FEED_EXPORT_BATCH_ITEM_COUNT": 10,
        "CLOSESPIDER_ITEMCOUNT": 40,

    }

    def get_url(self, url):
        payload = {
            "api_key": "4ef6e6e4556ef422401a3c40a78c9227",
            "url": url,
            "country_code": "eu",
            "device_type": "desktop",
            "session_number": 1,
        }
        proxy_url = "http://api.scraperapi.com/?" + urlencode(payload)
        return proxy_url

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=self.get_url(url), callback=self.parse)

    def parse(self, response):
        yield {
            # TODO: Define item fields
        }

        # TODO: Parse next pages and yield requests
        pass

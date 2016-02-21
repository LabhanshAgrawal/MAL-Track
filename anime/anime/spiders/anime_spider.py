import scrapy

from anime.items import AnimeItem

class AnimeSpider(scrapy.Spider):
    name = "anime"
    allowed_domains = ["myanimelist.net"]
    start_urls = [
        "http://myanimelist.net/animelist/labho/",
    ]

    def parse(self, response):
        target = open('/home/labhansh/labho', 'w')
        target.write(response.xpath('//*[@id="list-container"]/div[3]/div/table'))

import scrapy
from scrapy.http.response import Response
from Irodori.items import AuthorItem
from Irodori.items import ComicItem

class IrodoriSpider(scrapy.Spider):
    name = "irodori"
    allowed_domains = ["irodoricomics.com"]
    start_urls = ["https://irodoricomics.com/index.php?route=product/manufacturer"]

    def parse(self, response:Response):
        # print("结果",dir(response))
        # print("结果",vars(response))

        li_list = response.xpath('//*[@id="content"]/div/div')
        for li in li_list:
            url = li.xpath("./a/@href").extract_first()
            # print("结果url",url,type(url))
            # item = AuthorItem(
            #     url=li.xpath("./a/@href").extract_first(),
            #     name=li.xpath(".//span/text()").extract_first(),
            #     avatar=li.xpath(".//@src").extract_first(),
            # )
            # yield item
            # yield scrapy.Request(url=url, callback=self.parse_author)
            yield response.follow(url=url, callback=self.parse_author)

    def parse_author(self,response:Response):
        print("结果",response)
        urlList = response.xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/a/@href').extract()
        for url in urlList:
            # item = response.meta['item']
            # item['url'] = url
            # print("parse_author结果",url,type(url))
            yield response.follow(url=url, callback=self.parse_comic)
            # yield scrapy.Request(url=url, callback=self.parse_comic,meta={'item':item})

    def parse_comic(self,response:Response):
        print("parse_comic结果",response)
        urlList = response.xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/a/@href').extract()
        for url in urlList:
            yield response.follow(url=url, callback=self.parse_detail)

    def parse_detail(self,response:Response):
        print("parse_detail结果",response)
        item = ComicItem(
            title=response.xpath('/html/body/div[4]/h1/span/text()').extract_first(),
            author=response.xpath('//*[@id="product"]/div[3]/ul/li[1]/a/text()').extract_first(),
            jp_title=response.xpath('//*[@id="product"]/div[3]/ul/li[1]/a/text()').extract_first(),
            rm_title=response.xpath('//*[@id="product"]/div[3]/ul/li[4]/span/text()').extract_first(),
            pages=response.xpath('//*[@id="product"]/div[3]/ul/li[2]/span/text()').extract_first(),
        )
        print("parse_detail结果item",item)
        yield item
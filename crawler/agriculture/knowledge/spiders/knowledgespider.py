import scrapy
from knowledge.items import KnowledgeItem


class KnowledgespiderSpider(scrapy.Spider):
    name = "knowledgespider"
    allowed_domains = ["my478.com"]
    start_urls = ["https://www.my478.com/baike/list/"]
    request_headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    def parse(self, response):
        knowledge_item=KnowledgeItem()
        for knowledge_element in response.css('li.title'):
            title=knowledge_element.css('a::text').extract()
            url_str=knowledge_element.css('a::attr(href)').extract()
            link="https://www.my478.com"+url_str[0]
            create_time=knowledge_element.css('span::text').extract()
            # knowledge_item['title']=title
            # knowledge_item['link']=link
            # knowledge_item['create_time']=create_time
            yield scrapy.Request(url=link,headers=self.request_headers,callback=self.parse_linked_page,meta={'knowledge_item': knowledge_item,'title':title,'link':link,'create_time':create_time})
    
    def parse_linked_page(self,response):
        knowledge_item=response.meta['knowledge_item']
        title=response.meta['title']
        link=response.meta['link']
        create_time=response.meta['create_time']
        css_selector=response.css
        image=css_selector('div.center > img::attr(src)').extract()
        content=css_selector('div.content > p::text').extract()
        knowledge_item['title']=title
        knowledge_item['link']=link
        knowledge_item['create_time']=create_time
        knowledge_item['image']=image
        knowledge_item['content']=content
        yield knowledge_item

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,headers=self.request_headers, callback=self.parse)
        



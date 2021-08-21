import scrapy


class FlipkartphoneSpider(scrapy.Spider):
    name            = 'flipkartphone'
    allowed_domains = ['www.flipkart.com']
    start_urls      = ['https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1']

    def parse(self, response):
        for item_html in response.css("div._13oc-S > div"):
            link    = item_html.css("a.s1Q9rs::attr(href)").get()
            title   = item_html.css("a.s1Q9rs::text").get()
            yield {
                "current_page_link" : response.url,
                "link"              : response.urljoin(link),
                "title"             : title,
                "point"             : item_html.css("div._3LWZlK::text").get(),
                "price"             : item_html.css("div._30jeq3::text").get(),
            }
            
        #for next_page in response.css('a._1LKTO3'):  #_1LKTO3
        #    yield response.follow(next_page, self.parse)

import scrapy


class LinuxMintSpider(scrapy.Spider):
    name            = 'linux-mint'
    allowed_domains = ['linuxmint.com']
    start_urls      = ['https://linuxmint.com/edition.php?id=288']

    def parse(self, response):
        for item_html in response.css("table.sponsor-table tr"):
            row_html = item_html.css("td")
            if len(row_html) == 3:
                #print(row_html)
                img         = row_html[0].css("img::attr(src)").extract_first()
                location    = row_html[1].css("::text").extract_first()
                mirror      = row_html[2].css("a::text").extract_first()
                mirror_link = row_html[2].css("a::attr(href)").extract_first()
                yield{  
                    'img'           : response.urljoin(img),
                    'location'      : location,
                    'mirror'        : mirror,
                    'mirror_link'   : mirror_link
                }

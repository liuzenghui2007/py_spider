import scrapy
from py_parse.items import HypeAuditorItem

class HypeAuditorSpider(scrapy.Spider):
    name = 'hypeauditor'
    allowed_domains = ['hypeauditor.com']
    start_urls = ['https://hypeauditor.com/top-instagram-alcohol-united-states/']

    def parse(self, response):
        # Save the response body to a file for inspection
        filename = "hype.html"
        with open(filename, 'w') as f:
            f.write(response.body.decode('utf-8'))
        
        self.logger.info(f"Saved response to {filename}")

        # Extract data from the table rows
        for row in response.css('.table .row[data-v-bf890aa6]'):
            item = HypeAuditorItem()
            item['rank'] = row.css('.row-cell.rank span[data-v-bf890aa6]::text').get(default='').strip()
            item['nick'] = row.css('.contributor__content-username::text').get(default='').strip()
            item['firstName'] = row.css('.contributor__content-fullname::text').get(default='').strip()
            item['category'] = row.css('.row-cell.category .tag__content::text').get(default='').strip()
            item['followers'] = row.css('.row-cell.subscribers::text').get(default='').strip()
            item['country'] = row.css('.row-cell.audience::text').get(default='').strip()
            item['engAuth'] = row.css('.row-cell.authentic::text').get(default='').strip()
            item['engAvg'] = row.css('.row-cell.engagement::text').get(default='').strip()
            
            self.logger.debug(f"Extracted item: {item}")
            yield item 
import scrapy

class NoxInfluencerSaveSpider(scrapy.Spider):
    name = 'noxinfluencer'
    allowed_domains = ['cn.noxinfluencer.com']
    start_urls = ['https://cn.noxinfluencer.com/youtube-channel-rank/top-100-us-all-youtuber-sorted-by-subs-weekly']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            })

    def parse(self, response):
        # 保存网页内容到本地文件
        filename = 'noxinfluencer_top_100_us.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.logger.info(f'Saved file {filename}') 
import scrapy
from scrapy_splash import SplashRequest
import pandas as pd

class NoxinfluencerSpider(scrapy.Spider):
    name = 'noxinfluencer'
    allowed_domains = ['cn.noxinfluencer.com']
    start_urls = ['https://cn.noxinfluencer.com/youtube-channel-rank/top-100-us-all-youtuber-sorted-by-subs-weekly']

    script = """
    function main(splash, args)
      splash:set_user_agent(args.headers["User-Agent"])
      splash:init_cookies(splash.args.cookies)
      assert(splash:go(args.url))
      assert(splash:wait(5))
      return {
        html = splash:html(),
        cookies = splash:get_cookies(),
      }
    end
    """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url,
                self.parse,
                endpoint='execute',
                args={'lua_source': self.script, 'wait': 5},
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                    'Accept-Language': 'en-US,en;q=0.9',
                },
            )

    def parse(self, response):
        data = []
        rows = response.css('div#table-body > div.table-line.clearfix')
        for row in rows:
            rank_number = row.css('span.rank-number::text').get(default='').strip()
            description = row.css('span.rank-desc::text').get(default='').strip()
            category = row.css('span.rank-category::text').get(default='').strip()
            subscribers = row.css('span.rank-subs::text').get(default='').strip()
            avg_views = row.css('span.rank-avg-view::text').get(default='').strip()
            score = row.css('span.rank-score::text').get(default='').strip()

            data.append({
                "Rank": rank_number,
                "Description": description,
                "Category": category,
                "Subscribers": subscribers,
                "Avg Views": avg_views,
                "Score": score
            })

        # 将数据保存到 CSV 文件
        df = pd.DataFrame(data)
        df.to_csv('youtube_data_splash.csv', index=False, encoding='utf-8-sig') 
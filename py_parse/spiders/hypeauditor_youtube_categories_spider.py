import scrapy
from py_parse.items import HypeAuditorItem
import csv

class HypeAuditorYouTubeCategoriesSpider(scrapy.Spider):
    name = 'hypeauditor_youtube_categories'
    allowed_domains = ['hypeauditor.com']
    
    # 定义所有类别的 URI
    categories = {
        "All Categories": "/top-youtube-all-united-states/",
        "ASMR": "/top-youtube-asmr-united-states/",
        "Animals & Pets": "/top-youtube-animals-pets-united-states/",
        "Animation": "/top-youtube-animation-united-states/",
        "Autos & Vehicles": "/top-youtube-autos-vehicles-united-states/",
        "Beauty": "/top-youtube-beauty-united-states/",
        "DIY & Life Hacks": "/top-youtube-diy-life-hacks-united-states/",
        "Daily vlogs": "/top-youtube-daily-vlogs-united-states/",
        "Design/art": "/top-youtube-design-art-united-states/",
        "Education": "/top-youtube-education-united-states/",
        "Family & Parenting": "/top-youtube-family-parenting-united-states/",
        "Fashion": "/top-youtube-fashion-united-states/",
        "Fitness": "/top-youtube-fitness-united-states/",
        "Food & Drinks": "/top-youtube-food-drinks-united-states/",
        "Health & Self Help": "/top-youtube-health-self-help-united-states/",
        "Humor": "/top-youtube-humor-united-states/",
        "Movies": "/top-youtube-movies-united-states/",
        "Music & Dance": "/top-youtube-music-dance-united-states/",
        "Mystery": "/top-youtube-mystery-united-states/",
        "News & Politics": "/top-youtube-news-politics-united-states/",
        "Science & Technology": "/top-youtube-science-technology-united-states/",
        "Show": "/top-youtube-show-united-states/",
        "Sports": "/top-youtube-sports-united-states/",
        "Toys": "/top-youtube-toys-united-states/",
        "Travel": "/top-youtube-travel-united-states/",
        "Video games": "/top-youtube-video-games-united-states/"
    }

    def start_requests(self):
        base_url = 'https://hypeauditor.com'
        for category, uri in self.categories.items():
            url = base_url + uri
            yield scrapy.Request(url, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }, meta={'category': category})

    def parse(self, response):
        category = response.meta['category']
        self.logger.debug(f"Processing category: {category}")

        # Create or open the CSV file for each category
        filename = f'hypeauditor_youtube_{category.replace(" ", "_").lower()}.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['rank', 'channel_name', 'category', 'followers', 'views_avg', 'likes_avg', 'comments_avg'])

            # Extract data from the table rows
            for row in response.css('.table .row'):
                item = HypeAuditorItem()
                item['rank'] = row.css('.rank::text').get(default='').strip()
                item['channel_name'] = row.css('.channel-name::text').get(default='').strip()
                item['category'] = category
                item['followers'] = row.css('.followers::text').get(default='').strip()
                item['views_avg'] = row.css('.views-avg::text').get(default='').strip()
                item['likes_avg'] = row.css('.likes-avg::text').get(default='').strip()
                item['comments_avg'] = row.css('.comments-avg::text').get(default='').strip()

                # Write to the CSV file
                csv_writer.writerow([
                    item['rank'], item['channel_name'], item['category'],
                    item['followers'], item['views_avg'], item['likes_avg'], item['comments_avg']
                ])
        
        self.logger.info(f'Saved file {filename}') 
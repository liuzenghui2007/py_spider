import scrapy
from py_parse.items import HypeAuditorYouTubeCategoryItem
import csv

class HypeAuditorYouTubeCategoriesSpider(scrapy.Spider):
    name = 'hypeauditor_youtube_merge'
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
        # Create or open the CSV file
        self.file = open('hypeauditor_youtube_united_states_all_results.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow(['rank', 'influencer', 'category', 'followers', 'viewsAvg', 'likesAvg', 'commentsAvg', 'category_2'])

        # Iterate over all categories and their URIs
        for category, uri in self.categories.items():
            url = base_url + uri
            yield scrapy.Request(url, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }, meta={'category': category})

    def parse(self, response):
        category = response.meta['category']
        self.logger.debug(f"Processing category: {category}")


        # Extract data from the table rows
        rows = response.css('.table .row[data-v-bf890aa6]')
        for row in rows:
            item = HypeAuditorYouTubeCategoryItem()
            item['rank'] = row.css('.row-cell.rank span[data-v-bf890aa6]::text').get(default='').strip()
            item['influencer'] = row.css('.contributor__content-username::text').get(default='').strip()
            item['category'] = row.css('.row-cell.category .tag__content::text').get(default='').strip()
            item['followers'] = row.css('.row-cell.subscribers::text').get(default='').strip()
            item['viewsAvg'] = row.css('.row-cell.avg-views::text').get(default='').strip()
            item['likesAvg'] = row.css('.row-cell.avg-likes::text').get(default='').strip()
            item['commentsAvg'] = row.css('.row-cell.avg-comments::text').get(default='').strip()
            # Write to the CSV file
            self.csv_writer.writerow([
                item['rank'], item['influencer'], item['category'],
                item['followers'], item['viewsAvg'], item['likesAvg'], item['commentsAvg'], category
                ])
        
    def closed(self, reason):
        # Close the file when the spider is closed
        self.file.close() 
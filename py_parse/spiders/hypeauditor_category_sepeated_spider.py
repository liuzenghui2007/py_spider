import scrapy
from py_parse.items import HypeAuditorItem
import os

class HypeAuditorCategorySpider(scrapy.Spider):
    name = 'hypeauditor_category_seperated'
    allowed_domains = ['hypeauditor.com']
    
    categories = {
        "Accessories & Jewellery": "/top-instagram-accessories-jewellery-united-states/",
        "Adult content": "/top-instagram-adult-content-united-states/",
        "Alcohol": "/top-instagram-alcohol-united-states/",
        "Animals": "/top-instagram-animals-united-states/",
        "Architecture & Urban Design": "/top-instagram-architecture-urban-design-united-states/",
        "Art/Artists": "/top-instagram-art-artists-united-states/",
        "Beauty": "/top-instagram-beauty-united-states/",
        "Business & Careers": "/top-instagram-business-careers-united-states/",
        "Cars & Motorbikes": "/top-instagram-cars-motorbikes-united-states/",
        "Cinema & Actors/actresses": "/top-instagram-cinema-actors-actresses-united-states/",
        "Clothing & Outfits": "/top-instagram-clothing-outfits-united-states/",
        "Comics & sketches": "/top-instagram-comics-sketches-united-states/",
        "Computers & Gadgets": "/top-instagram-computers-gadgets-united-states/",
        "Crypto": "/top-instagram-crypto-united-states/",
        "DIY & Design": "/top-instagram-diy-design-united-states/",
        "Education": "/top-instagram-education-united-states/",
        "Extreme Sports & Outdoor activity": "/top-instagram-extreme-sports-outdoor-activity-united-states/",
        "Family": "/top-instagram-family-united-states/",
        "Fashion": "/top-instagram-fashion-united-states/",
        "Finance & Economics": "/top-instagram-finance-economics-united-states/",
        "Fitness & Gym": "/top-instagram-fitness-gym-united-states/",
        "Food & Cooking": "/top-instagram-food-cooking-united-states/",
        "Gaming": "/top-instagram-gaming-united-states/",
        "Health & Medicine": "/top-instagram-health-medicine-united-states/",
        "Humor & Fun & Happiness": "/top-instagram-humor-fun-happiness-united-states/",
        "Kids & Toys": "/top-instagram-kids-toys-united-states/",
        "Lifestyle": "/top-instagram-lifestyle-united-states/",
        "Literature & Journalism": "/top-instagram-literature-journalism-united-states/",
        "Luxury": "/top-instagram-luxury-united-states/",
        "Machinery & Technologies": "/top-instagram-machinery-technologies-united-states/",
        "Management & Marketing": "/top-instagram-management-marketing-united-states/",
        "Mobile related": "/top-instagram-mobile-related-united-states/",
        "Modeling": "/top-instagram-modeling-united-states/",
        "Music": "/top-instagram-music-united-states/",
        "NFT": "/top-instagram-nft-united-states/",
        "Nature & landscapes": "/top-instagram-nature-landscapes-united-states/",
        "Photography": "/top-instagram-photography-united-states/",
        "Racing Sports": "/top-instagram-racing-sports-united-states/",
        "Science": "/top-instagram-science-united-states/",
        "Shopping & Retail": "/top-instagram-shopping-retail-united-states/",
        "Shows": "/top-instagram-shows-united-states/",
        "Sports with a ball": "/top-instagram-sports-with-a-ball-united-states/",
        "Sweets & Bakery": "/top-instagram-sweets-bakery-united-states/",
        "Tobacco & Smoking": "/top-instagram-tobacco-smoking-united-states/",
        "Trainers & Coaches": "/top-instagram-trainers-coaches-united-states/",
        "Travel": "/top-instagram-travel-united-states/",
        "Water sports": "/top-instagram-water-sports-united-states/",
        "Winter sports": "/top-instagram-winter-sports-united-states/",
    }
    
    def start_requests(self):
        base_url = 'https://hypeauditor.com'
        for category, path in self.categories.items():
            url = base_url + path
            yield scrapy.Request(url, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }, meta={'category': category})

    def parse(self, response):
        category = response.meta['category']
        # Create a directory to store CSV files
        directory = 'hypeauditor_results'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Prepare the filename
        filename = os.path.join(directory, f"{category.replace('/', ' ').replace('&', 'and')}.csv")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('rank,nick,firstName,category,followers,country,engAuth,engAvg\n')
            for row in response.css('.table .row[data-v-40a1893f]'):
                item = HypeAuditorItem()
                item['rank'] = row.css('.row-cell.rank span[data-v-40a1893f]::text').get(default='').strip()
                item['nick'] = row.css('.contributor__content-username::text').get(default='').strip()
                item['firstName'] = row.css('.contributor__content-fullname::text').get(default='').strip()
                item['category'] = row.css('.row-cell.category .tag__content::text').get(default='').strip()
                item['followers'] = row.css('.row-cell.subscribers::text').get(default='').strip()
                item['country'] = row.css('.row-cell.audience::text').get(default='').strip()
                item['engAuth'] = row.css('.row-cell.authentic::text').get(default='').strip()
                item['engAvg'] = row.css('.row-cell.engagement::text').get(default='').strip()
                
                f.write(f"{item['rank']},{item['nick']},{item['firstName']},{item['category']},{item['followers']},{item['country']},{item['engAuth']},{item['engAvg']}\n") 
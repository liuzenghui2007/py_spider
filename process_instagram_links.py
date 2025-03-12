import pandas as pd
import re

def extract_shopping_links(links_str):
    if pd.isna(links_str):
        return ''
        
    # 定义社交媒体域名
    social_media_domains = [
        'youtube.com', 'www.youtube.com', 
        'facebook.com', 'www.facebook.com', 
        'twitter.com', 'www.twitter.com', 
        'instagram.com', 'www.instagram.com', 
        'tiktok.com', 'www.tiktok.com', 
        'snapchat.com', 'www.snapchat.com', 
        'pinterest.com', 'www.pinterest.com', 
        'linkedin.com', 'www.linkedin.com',
        'discord.gg', 'www.discord.gg',
        'bit.ly', 'www.bit.ly',
        'reddit.com', 'www.reddit.com',
        'vm.tiktok.com',
        'linktr.ee', 'www.linktr.ee'
    ]
    
    # 分割链接（考虑到可能的分隔符）
    links = [link.strip() for link in links_str.split(',') if link.strip()]
    
    # 提取购物链接
    shopping_links = []
    for link in links:
        # 清理链接末尾的标点符号
        link = re.sub(r'[.,;:!?)]$', '', link)
        
        # 提取域名
        domain_match = re.findall(r'https?://([^/]+)', link)
        if domain_match:
            domain = domain_match[0]
            # 检查是否为社交媒体域名
            if not any(social_domain in domain.lower() for social_domain in social_media_domains):
                shopping_links.append(link)
    
    return '\n'.join(shopping_links) if shopping_links else ''

def main():
    # 读取 CSV 文件
    df = pd.read_csv('instagram_influencer.csv')
    
    # 确保 'Bio Links' 列存在
    if 'Bio Links' not in df.columns:
        print("Error: 'Bio Links' column not found in CSV file")
        return
    
    # 添加新列 'Shopping Links'
    df['Shopping Links'] = df['Bio Links'].apply(extract_shopping_links)
    
    # 保存结果到新的 CSV 文件
    df.to_csv('instagram_influencer_with_shopping_links.csv', index=False, encoding='utf-8-sig')
    print("Processing completed. Results saved to 'instagram_influencer_with_shopping_links.csv'")

if __name__ == "__main__":
    main() 
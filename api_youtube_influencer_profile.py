# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list using API Key
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import re
import pandas as pd
import googleapiclient.discovery
import googleapiclient.errors

def extract_shopping_domains(links):
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
        'vm.tiktok.com'
    ]
    
    # 提取购物域名
    shopping_links = []
    # 清理链接，去掉多余的换行符和空格
    cleaned_links = [link.strip() for link in links if link.strip()]
    
    for link in cleaned_links:
        domain = re.findall(r'https?://([^/]+)', link)
        if domain:
            domain = domain[0]
            # 检查是否为社交媒体域名
            if not any(social_domain in domain for social_domain in social_media_domains):
                shopping_links.append(link)
    
    return shopping_links

def main():
    # YouTube API 服务名称和版本
    api_service_name = "youtube"
    api_version = "v3"
    
    # 你的 API Key
    api_key = "AIzaSyDwOV_XUeKCS5FvP6R3N8PgWMdnhBGOsjY"  # 替换为你的 API Key

    # 创建 API 客户端
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    # 读取 YouTube influencer CSV 文件
    influencers_df = pd.read_csv('youyou.csv')  # 确保文件路径正确
    results = []

    for index, row in influencers_df.iterrows():
        # 跳过前79行
        if index < 79 or index > 90:
            continue
            
        handle = row['contributorContentUsername']  # 使用 'Handle' 列
        if pd.isna(handle):  # 跳过空值
            continue
            
        print(f"\nProcessing row {index + 1}: {handle}")  # 显示当前处理的行
        
        # 发起请求获取频道信息
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            forHandle=handle  # 使用 CSV 中的频道自定义 URL
        )
        response = request.execute()

        # 提取所需信息
        if response.get('items'):
            channel_info = response['items'][0]  # 获取第一个频道的信息
            title = channel_info['snippet']['title']
            description = channel_info['snippet']['description']
            subscribers = channel_info['statistics']['subscriberCount']
            video_count = channel_info['statistics']['videoCount']
            view_count = channel_info['statistics']['viewCount']
            published_at = channel_info['snippet']['publishedAt']

            print(f"Found channel: {title}")
            print(f"Subscribers: {subscribers}")
            print(f"Video Count: {video_count}")
            print(f'description', {description})

            # 提取链接
            links = re.findall(r'http[s]?://[^\s]+', description)
            
            # 清理链接，去掉链接末尾的标点符号
            cleaned_links = []
            for link in links:
                # 去掉链接末尾的标点符号
                link = re.sub(r'[.,;:!?)]$', '', link)
                cleaned_links.append(link)

            # 提取购物链接
            shopping_links = extract_shopping_domains(cleaned_links)
            
            if shopping_links:
                print(f"Found {len(shopping_links)} shopping links")

            # 将结果添加到列表
            results.append({
                'Handle': handle,
                'Channel Title': title,
                'Description': description,
                'Subscribers': subscribers,
                'Video Count': video_count,
                'View Count': view_count,
                'Published At': published_at,
                'Links': '\n'.join(cleaned_links),  # 使用换行符连接所有链接
                'Shopping Links': '\n'.join(shopping_links)  # 使用换行符连接购物链接
            })
        else:
            results.append({
                'Handle': handle,
                'Channel Title': None,
                'Description': None,
                'Subscribers': None,
                'Video Count': None,
                'View Count': None,
                'Published At': None,
                'Links': None,
                'Shopping Links': None
            })

    # 将结果保存到新的 CSV 文件
    results_df = pd.DataFrame(results)
    results_df.to_csv('youyou2.csv', index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    main()
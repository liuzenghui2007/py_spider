# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list using API Key
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import re
import pandas as pd
import googleapiclient.discovery
import googleapiclient.errors

def main():
    # YouTube API 服务名称和版本
    api_service_name = "youtube"
    api_version = "v3"
    
    # 你的 API Key
    api_key = "AIzaSyCEw2Dcj_q4lTKOYz8TLWD-KxJ73DjgwKM"  # 替换为你的 API Key

    # 创建 API 客户端
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    # 读取 YouTube influencer CSV 文件
    influencers_df = pd.read_csv('youtube influencer.csv')  # 确保文件路径正确
    results = []

    for index, row in influencers_df.iterrows():
        handle = row['contributorContentUsername']  # 使用 'userName' 列
        
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

            # 提取链接
            links = re.findall(r'http[s]?://[^\s]+', description)

            # 将结果添加到列表
            results.append({
                'Handle': handle,
                'Channel Title': title,
                'Description': description,
                'Subscribers': subscribers,
                'Video Count': video_count,
                'View Count': view_count,
                'Published At': published_at,
                'Links': '\n'.join(links)  # 使用换行符连接链接
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
                'Links': None
            })

    # 将结果保存到新的 CSV 文件
    results_df = pd.DataFrame(results)
    results_df.to_csv('youtube_influencer_results.csv', index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    main()
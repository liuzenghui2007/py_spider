# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list using API Key
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import re
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

    # 发起请求获取频道信息
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forHandle="@Allure"  # 替换为你想要查询的频道的自定义 URL
    )
    response = request.execute()

    # 提取所需信息
    channel_info = response.get('items', [])[0]  # 获取第一个频道的信息
    title = channel_info['snippet']['title']
    description = channel_info['snippet']['description']
    subscribers = channel_info['statistics']['subscriberCount']
    video_count = channel_info['statistics']['videoCount']
    view_count = channel_info['statistics']['viewCount']
    published_at = channel_info['snippet']['publishedAt']

    # 提取链接
    links = re.findall(r'http[s]?://[^\s]+', description)

    # 打印频道信息
    print(f"Channel Title: {title}")
    print(f"Description: {description}")
    print(f"Subscribers: {subscribers}")
    print(f"Video Count: {video_count}")
    print(f"View Count: {view_count}")
    print(f"Published At: {published_at}")

    # 打印提取的链接
    if links:
        print("Extracted Links:")
        for link in links:
            print(link)

    # 如果你想处理多个频道，可以这样做：
    # handles = ["@GoogleDevelopers", "@YouTube", "@GoogleCreators"]
    # for handle in handles:
    #     request = youtube.channels().list(
    #         part="snippet,contentDetails,statistics",
    #         forHandle=handle
    #     )
    #     response = request.execute()
    #     print(f"Channel: {handle}")
    #     print(response)

if __name__ == "__main__":
    main()
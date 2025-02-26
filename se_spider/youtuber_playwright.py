import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def main():
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 导航到目标页面
        await page.goto("https://cn.noxinfluencer.com/youtube-channel-rank/top-100-us-all-youtuber-sorted-by-subs-weekly")

        # 等待表格加载
        await page.wait_for_selector('#table-body')

        # 滚动到页面底部以加载所有内容
        previous_height = await page.evaluate("document.body.scrollHeight")
        while True:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(2000)  # 等待新内容加载
            new_height = await page.evaluate("document.body.scrollHeight")
            if new_height == previous_height:
                break
            previous_height = new_height

        # 提取数据
        data = []
        rows = await page.query_selector_all('div#table-body > div.table-line.clearfix')
        for row in rows:
            rank_number_element = await row.query_selector('span.rank-number')
            description_element = await row.query_selector('span.rank-desc')
            category_element = await row.query_selector('span.rank-category')
            subscribers_element = await row.query_selector('span.rank-subs')
            avg_views_element = await row.query_selector('span.rank-avg-view')
            score_element = await row.query_selector('span.rank-score')

            rank_number = await rank_number_element.inner_text() if rank_number_element else ''
            description = await description_element.inner_text() if description_element else ''
            category = await category_element.inner_text() if category_element else ''
            subscribers = await subscribers_element.inner_text() if subscribers_element else ''
            avg_views = await avg_views_element.inner_text() if avg_views_element else ''
            score = await score_element.inner_text() if score_element else ''

            data.append({
                "Rank": rank_number.strip(),
                "Description": description.strip(),
                "Category": category.strip(),
                "Subscribers": subscribers.strip(),
                "Avg Views": avg_views.strip(),
                "Score": score.strip()
            })

        # 关闭浏览器
        await browser.close()

        # 将数据转换为 DataFrame 并保存为 CSV
        df = pd.DataFrame(data)
        df.to_csv('youtube_data_playwright.csv', index=False, encoding='utf-8-sig')

# 运行异步主函数
asyncio.run(main()) 
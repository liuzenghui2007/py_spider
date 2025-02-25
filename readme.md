保存数据
scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：

scrapy crawl itcast -o teachers.json
scrapy crawl itcast -o teachers.jsonl
scrapy crawl itcast -o teachers.csv
scrapy crawl itcast -o teachers.xml

业务逻辑都在spiders中
items.py只是定义类字段


scrapy crawl hypeauditor -L DEBUG

# 抓取一个页面
scrapy crawl hypeauditor -o h.csv

# 新建文件夹，抓取所有分类页面，分别保存到单独的文件
scrapy crawl hypeauditor_category

# 合并49个分类的结果，保存到一个csv，最后一列标注category
scrapy crawl hypeauditor_category_merge

# proxy作为可选参数
scrapy crawl hypeauditor -s USE_PROXIES=True

# 
scrapy crawl hypeauditor_youtube_categories -s USE_PROXIES=True



scrapy crawl noxinfluencer -o noxinfluencer_us.csv
scrapy crawl noxinfluencer -o noxinfluencer_us.csv -s USE_PROXIES=True
scrapy crawl noxinfluencer -o noxinfluencer_us.csv -L DEBUG

#!/bin/bash
# 环境名
ENV_NAME=spider
# 创建虚拟环境并安装 Scrapy
conda create --name $ENV_NAME python=3.13 -y && \
conda activate $ENV_NAME && \
conda install -c conda-forge scrapy -y && \
scrapy --version


conda env create -f environment.yml
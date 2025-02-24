
保存数据
scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：

scrapy crawl itcast -o teachers.json
json lines格式，默认为Unicode编码

scrapy crawl itcast -o teachers.jsonl
csv 逗号表达式，可用Excel打开

scrapy crawl itcast -o teachers.csv
xml格式

scrapy crawl itcast -o teachers.xml

业务逻辑都在spiders中
items.py只是定义类字段


scrapy crawl hypeauditor -L DEBUG
scrapy crawl hypeauditor -o h.csv

# 新建文件夹，抓取所有分类页面，分别保存到单独的文件
scrapy crawl hypeauditor_category


#!/bin/bash
# 环境名
ENV_NAME=spider
# 创建虚拟环境并安装 Scrapy
conda create --name $ENV_NAME python=3.13 -y && \
conda activate $ENV_NAME && \
conda install -c conda-forge scrapy -y && \
scrapy --version


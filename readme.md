
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
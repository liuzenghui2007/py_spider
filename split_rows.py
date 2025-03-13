import pandas as pd
import csv

def clean_url(url):
    """清理URL字符串"""
    url = str(url).strip()
    url = url.strip('"').strip(',')  # 移除引号和逗号
    return url

def split_rows(input_file, output_file):
    """
    读取CSV文件，根据E-commerce Domains列中的URL进行行拆分
    
    参数:
        input_file: 输入CSV文件路径
        output_file: 输出CSV文件路径
    """
    try:
        # 使用csv模块读取文件
        new_rows = []
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # 读取标题行
            headers = next(reader)
            
            # 确保列名正确
            username_idx = 0  # Username列索引
            bio_links_idx = 1  # Bio Links列索引
            ecommerce_idx = 2  # E-commerce Domains列索引
            
            # 遍历数据行
            for row_num, row in enumerate(reader, start=2):  # start=2 因为第1行是标题
                try:
                    # 确保至少有3列数据
                    while len(row) < 3:
                        row.append('')
                    
                    username = str(row[username_idx]).strip()
                    bio_links = clean_url(row[bio_links_idx])
                    ecommerce = str(row[ecommerce_idx]).strip()
                    
                    # 如果是空值或"No e-commerce sites."，保留为空
                    if not ecommerce or ecommerce.lower() == 'no e-commerce sites.':
                        new_rows.append({
                            'Username': username,
                            'Bio Links': bio_links,
                            'E-commerce Domains': ''
                        })
                    else:
                        # 处理可能的多个域名
                        # 首先按换行分割，然后处理可能的逗号分割
                        domains = []
                        for d in ecommerce.split('\n'):
                            domains.extend([x.strip() for x in d.split(',') if x.strip()])
                        
                        # 过滤掉无效域名
                        domains = [d for d in domains if d and d.lower() != 'no e-commerce sites.']
                        
                        if not domains:
                            # 如果没有有效域名
                            new_rows.append({
                                'Username': username,
                                'Bio Links': bio_links,
                                'E-commerce Domains': ''
                            })
                        else:
                            # 对每个域名创建新行
                            for domain in domains:
                                new_rows.append({
                                    'Username': username,
                                    'Bio Links': bio_links,
                                    'E-commerce Domains': clean_url(domain)
                                })
                except Exception as e:
                    print(f"处理第 {row_num} 行时出错: {str(e)}")
                    print(f"行内容: {row}")
                    continue
        
        # 创建DataFrame并保存
        new_df = pd.DataFrame(new_rows)
        new_df.to_csv(
            output_file,
            index=False,
            quoting=csv.QUOTE_MINIMAL,
            encoding='utf-8'
        )
        print(f"处理完成，结果已保存到: {output_file}")
        print(f"拆分后行数: {len(new_df)}")
        
    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")


def main():
    input_file = 'instagram_influencer_ecommerce.csv'
    output_file = 'instagram_influencer_ecommerce_split.csv'
    split_rows(input_file, output_file)


if __name__ == "__main__":
    main()

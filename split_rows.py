import pandas as pd

def split_rows(input_file, output_file):
    """
    读取CSV文件，根据E-commerce Domains列中的URL进行行拆分
    
    参数:
        input_file: 输入CSV文件路径
        output_file: 输出CSV文件路径
    """
    # 读取CSV文件
    df = pd.read_csv(input_file)
    
    # 创建新的行列表
    new_rows = []
    
    # 遍历每一行
    for _, row in df.iterrows():
        # 获取E-commerce Domains中的URL列表
        domains = str(row['E-commerce Domains']).strip().split('\n')
        
        # 过滤掉空值和nan
        domains = [d.strip() for d in domains if d.strip() and d.strip().lower() != 'nan']
        
        if not domains:
            # 如果没有域名，保留原行，域名设为空
            new_rows.append({
                'Username': row['Username'],
                'Bio Links': row['Bio Links'],
                'E-commerce Domains': ''
            })
        else:
            # 对每个域名创建新行
            for domain in domains:
                new_rows.append({
                    'Username': row['Username'],
                    'Bio Links': row['Bio Links'],
                    'E-commerce Domains': domain
                })
    
    # 创建新的DataFrame并保存
    new_df = pd.DataFrame(new_rows)
    new_df.to_csv(output_file, index=False)
    print(f"处理完成，结果已保存到: {output_file}")
    print(f"原始行数: {len(df)}, 拆分后行数: {len(new_df)}")


def main():
    input_file = 'instagram_influencer_ecommerce.csv'
    output_file = 'instagram_influencer_ecommerce_split.csv'
    
    try:
        split_rows(input_file, output_file)
    except Exception as e:
        print(f"处理过程中出现错误: {str(e)}")


if __name__ == "__main__":
    main()

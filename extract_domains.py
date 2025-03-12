import re
from urllib.parse import urlparse

def extract_domains(file_path):
    domains = set()  # 使用集合来自动处理重复的域名

    with open(file_path, 'r') as file:
        for line in file:
            # 清理行
            url = line.strip()
            if not url:
                continue
                
            # 确保 URL 有协议前缀
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
                
            try:
                # 使用 urlparse 提取域名
                parsed_url = urlparse(url)
                domain = parsed_url.netloc or parsed_url.path
                
                # 去掉 www 前缀
                if domain.startswith('www.'):
                    domain = domain.replace('www.', '', 1)
                    
                # 去掉路径部分（如果没有正确解析）
                domain = domain.split('/')[0]
                
                if domain:
                    domains.add(domain)
            except Exception as e:
                print(f"处理 URL 时出错: {url}, 错误: {e}")

    return sorted(domains)  # 返回排序后的域名列表

def main():
    input_file = 'url.txt'  # 输入文件
    output_file = 'unique_domains.txt'  # 输出文件

    unique_domains = extract_domains(input_file)

    # 将结果写入输出文件
    with open(output_file, 'w') as file:
        for domain in unique_domains:
            file.write(f"{domain}\n")

    print(f"提取的唯一域名数量: {len(unique_domains)}")
    print(f"提取的唯一域名已保存到 {output_file}")

if __name__ == "__main__":
    main() 
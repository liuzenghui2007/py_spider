import tldextract

def extract_domains(file_path):
    domains = set()  # 使用集合来自动处理重复的域名

    with open(file_path, 'r') as file:
        for line in file:
            # 清理行
            url = line.strip()
            if not url:
                continue
                
            try:
                # 使用 tldextract 提取域名
                ext = tldextract.extract(url)
                
                # 组合子域名、域名和顶级域名，但排除 www 子域名
                if ext.domain and ext.suffix:
                    # 如果有子域名且不是 www，则包含它
                    if ext.subdomain and ext.subdomain != 'www':
                        domain = f"{ext.subdomain}.{ext.domain}.{ext.suffix}"
                    else:
                        domain = f"{ext.domain}.{ext.suffix}"
                    domains.add(domain)
            except Exception as e:
                print(f"处理 URL 时出错: {url}, 错误: {e}")

    return sorted(domains)  # 返回排序后的域名列表

def main():
    input_file = 'url.txt'  # 输入文件
    output_file = 'unique_domains.txt'  # 输出文件

    # 确保已安装 tldextract
    try:
        import tldextract
    except ImportError:
        print("请先安装 tldextract 库: pip install tldextract")
        return

    unique_domains = extract_domains(input_file)

    # 将结果写入输出文件
    with open(output_file, 'w') as file:
        for domain in unique_domains:
            file.write(f"{domain}\n")

    print(f"提取的唯一域名数量: {len(unique_domains)}")
    print(f"提取的唯一域名已保存到 {output_file}")

if __name__ == "__main__":
    main() 
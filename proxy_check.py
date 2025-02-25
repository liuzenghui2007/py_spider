import csv
import requests
from concurrent.futures import ThreadPoolExecutor

# 读取代理列表
def read_proxies(file_path):
    proxies = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            proxies.append(row)
    return proxies

# 检查代理是否可用
def check_proxy(proxy):
    ip = proxy['ip']
    port = proxy['port']
    proxy_url = f"http://{ip}:{port}"
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    try:
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        if response.status_code == 200:
            proxy['status'] = 'Working'
        else:
            proxy['status'] = 'Not Working'
    except requests.exceptions.RequestException:
        proxy['status'] = 'Not Working'
    return proxy

# 更新代理列表
def update_proxies(proxies, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = proxies[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for proxy in proxies:
            writer.writerow(proxy)

def main():
    file_path = 'proxies.csv'
    proxies = read_proxies(file_path)

    # 使用线程池并行检查代理
    with ThreadPoolExecutor(max_workers=10) as executor:
        updated_proxies = list(executor.map(check_proxy, proxies))

    update_proxies(updated_proxies, file_path)
    print("Proxy status updated.")

if __name__ == "__main__":
    main()
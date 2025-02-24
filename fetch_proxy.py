import requests
from bs4 import BeautifulSoup
import csv
import time

def fetch_proxies():
    print("Fetching proxies...")
    url = 'https://www.sslproxies.org/'  # Example proxy list website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        proxies = []
        table = soup.find('table', {'class': 'table table-striped table-bordered'})
        if table:
            for row in table.find('tbody').find_all('tr'):
                columns = row.find_all('td')
                if columns:
                    ip = columns[0].text.strip()
                    port = columns[1].text.strip()
                    country = columns[3].text.strip()
                    anonymity = columns[4].text.strip()
                    https = columns[6].text.strip()
                    proxies.append({
                        'ip': ip,
                        'port': port,
                        'country': country,
                        'anonymity': anonymity,
                        'https': https
                    })
        
        print(f"Fetched {len(proxies)} proxies.")
        return proxies
    except requests.RequestException as e:
        print(f"Error fetching proxies: {e}")
        return []

def test_proxy(proxy):
    test_url = 'http://httpbin.org/ip'
    proxies = {
        'http': f'http://{proxy["ip"]}:{proxy["port"]}',
        'https': f'https://{proxy["ip"]}:{proxy["port"]}',
    }
    try:
        start_time = time.time()
        response = requests.get(test_url, proxies=proxies, timeout=5)
        latency = time.time() - start_time
        if response.status_code == 200:
            return True, response.json().get('origin'), latency
    except requests.RequestException as e:
        print(f"Proxy {proxy['ip']}:{proxy['port']} failed: {e}")
        return False, None, None
    return False, None, None

def save_proxies_to_csv(proxies, filename='proxies.csv'):
    print("Testing and saving proxies...")
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ip', 'port', 'country', 'anonymity', 'https', 'status', 'origin', 'latency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for proxy in proxies:
            is_working, origin, latency = test_proxy(proxy)
            proxy['status'] = 'Working' if is_working else 'Not Working'
            proxy['origin'] = origin if is_working else ''
            proxy['latency'] = f"{latency:.2f} seconds" if latency else ''
            writer.writerow(proxy)
            print(f"{proxy['ip']}:{proxy['port']} - {proxy['status']}")

if __name__ == '__main__':
    proxies = fetch_proxies()
    save_proxies_to_csv(proxies)
    print(f"Tested and saved {len(proxies)} proxies to proxies.csv")
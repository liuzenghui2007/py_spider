import requests

def test_noxinfluencer_access():
    url = 'https://cn.noxinfluencer.com/youtube-channel-rank/top-100-us-all-youtuber-sorted-by-subs-weekly'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    try:
        response = requests.get(url, headers=headers)
        print(f'Status Code: {response.status_code}')
        if response.status_code == 403:
            print("Access denied. The server returned a 403 Forbidden status.")
        else:
            print("Response Headers:", response.headers)
            print("Response Content:", response.text[:500])  # Print first 500 characters of the response content
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_noxinfluencer_access()
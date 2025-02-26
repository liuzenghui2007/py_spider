# SE Spider

This project is a web scraping tool that uses Selenium and BeautifulSoup to extract data from websites. It requires a few Python packages and a ChromeDriver to be set up correctly.

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd se_spider
   ```

2. **Install required Python packages**:
   Make sure you have `pip` installed. Then run the following commands to install the necessary packages:
   ```bash
   pip install webdriver-manager
   pip install pandas
   ```

3. **Download ChromeDriver**:
   The `webdriver_manager` package can automatically download the appropriate version of ChromeDriver for you. However, if you need to download it manually due to network restrictions, follow these steps:
   
   - Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).
   - Download the version that matches your installed version of Chrome.
   - Extract the downloaded file and place the `chromedriver` executable in a directory of your choice.
   - Update your script to use the path to your downloaded `chromedriver`:
     ```python
     from selenium import webdriver
     from selenium.webdriver.chrome.service import Service

     service = Service('/path/to/chromedriver')  # Update this path
     driver = webdriver.Chrome(service=service)
     ```

## Usage

- Run your script using Python:
  ```bash
  python your_script.py
  ```

## Troubleshooting

- **Network Issues**: If you encounter issues with downloading ChromeDriver automatically, ensure your network connection is stable or try downloading it manually as described above.
- **Firewall/Proxy**: If you're behind a firewall or proxy, ensure that your network settings allow access to external sites.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
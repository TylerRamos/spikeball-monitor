import requests
import time
from datetime import datetime

def log(message):
    print("[{}] {}".format(datetime.now().strftime("%H:%M:%S%f")[0:-5], message))
        
class Spikeball:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "referer": "https://spikeball.com/collections/pro-set/products/dunkin",
        "sec-ch-ua": '''"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"''',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '''"Windows"''',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
        
    def pull_stock(self, product_url):
        response = self.session.request("GET", product_url, headers=self.headers)
        inventory_quantity = response.json()["product"]["variants"][0]["inventory_quantity"]
        return inventory_quantity
    
    def monitor(self, product_url, interval):
        while True:
            if self.pull_stock(product_url) > 0:
                log("In stock")
            else:
                log("Out of stock")
            time.sleep(interval)

if __name__ == "__main__":
    spikeball = Spikeball()
    spikeball.monitor("https://spikeball.com/products/dunkin", 1)

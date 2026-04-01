import requests
from bs4 import BeautifulSoup
from datetime import datetime

class NewsScraper:
    def __init__(self):
        # User-Agent makes the script look like a real browser to avoid being blocked
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def fetch_bbc_tech(self):
        url = "https://www.bbc.com/innovation/technology"
        headlines = []
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            
            # 1. TRY SPECIFIC CLASS FIRST
            articles = soup.find_all('h2', class_='sc-4fedabc7-3')
            
            # 2. BACKUP: If empty, find all <h2> tags (BBC usually uses h2 for headlines)
            if not articles:
                articles = soup.find_all('h2')

            for item in articles[:10]:
                title = item.get_text(strip=True)
                if len(title) > 10: # Ignore tiny fragments
                    headlines.append({
                        "Source": "BBC Tech",
                        "Headline": title,
                        "Time": datetime.now().strftime("%H:%M")
                    })
        except Exception as e:
            print(f"Error scraping BBC: {e}")
        return headlines

    def fetch_reuters_tech(self):
        url = "https://www.reuters.com/technology/"
        headlines = []
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Reuters backup logic: look for h3 tags or specific heading classes
            articles = soup.find_all(['h3', 'h2'])
            
            for item in articles[:10]:
                title = item.get_text(strip=True)
                if len(title) > 15:
                    headlines.append({
                        "Source": "Reuters",
                        "Headline": title,
                        "Time": datetime.now().strftime("%H:%M")
                    })
        except Exception as e:
            print(f"Error scraping Reuters: {e}")
        return headlines
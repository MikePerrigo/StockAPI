import requests

class StockSearch:
    def __init__(self, ticker: str):
        self.ticker = ticker

    def search(self):
        self.api_key = "1JHo7I0oPuNeNpTjmMCuZURwTH9iWzxg"
        self.searh_url = f'https://financialmodelingprep.com/api/v3/search?query={self.ticker}&apikey={self.api_key}'
        r = requests.get(self.searh_url)
        if not r.json():
            raise ValueError("Ticker not found!")
        else:
            return r


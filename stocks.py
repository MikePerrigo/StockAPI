import requests


class Stock:
    def __init__(self, ticker: str = None):
        self.ticker = ticker
        self.api_key = "1JHo7I0oPuNeNpTjmMCuZURwTH9iWzxg"
        self.search_url = f'https://financialmodelingprep.com/api/v3/search?query={self.ticker}&apikey={self.api_key}'
        self.live_quote_url = f'https://financialmodelingprep.com/api/v3/quote/{self.ticker}?apikey={self.api_key}'

    def search(self):
        r = requests.get(self.search_url)
        if not r.json():
            raise ValueError("Ticker not found!")
        else:
            return r

    def live_quote(self):
        r = requests.get(self.live_quote_url)
        return r.json()


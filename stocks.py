import pprint

import requests

class Stock:
    stock_volatility_list = []
    def __init__(self, ticker: str = None):
        self.ticker = ticker
        self.api_key = "1JHo7I0oPuNeNpTjmMCuZURwTH9iWzxg"
        # Check that the ticker is listed
        self.search()

    def search(self):
        searh_url = f'https://financialmodelingprep.com/api/v3/search?query={self.ticker}&apikey={self.api_key}'
        r = requests.get(searh_url)
        if not r.json():
            raise ValueError("Ticker not found!")
        else:
            return r

    def live_quote(self):
        quote_url = f'https://financialmodelingprep.com/api/v3/quote/{self.ticker}?apikey={self.api_key}'
        r = requests.get(quote_url)
        return r.json()

    def volatility_builder(self):
        """
        TO-DO: Get rid of this once stock_evaluation.py is working as expected
        :return:
        """
        r = self.live_quote()
        if r[0]['changesPercentage'] >= 1:
            self.stock_volatility_list.append(self.ticker)
            print(f'Added {self.ticker}')
        else:
            print(f'Not adding {self.ticker}')

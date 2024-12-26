import pytest
import pprint
from stocks import Stock
import stock_evaluation as evaluation

def test_search_google():
    stock = Stock("GOOG")
    r = stock.search()
    stock_info = r.json()
    assert stock_info[0]['stockExchange'] == 'NASDAQ Global Select'
    assert stock_info[0]['name'] == 'Alphabet Inc.'

@pytest.mark.parametrize("ticker", ["AAPL","META", "GOOG", "NFLX"])
def test_search_input(ticker):
    stock = Stock(ticker)
    r = stock.search()
    stock_info = r.json()
    pprint.pprint(stock_info[0])

def test_invalid_ticker():
    stock = Stock("GOOG")
    r = stock.search()
    stocks = r.json()
    nyse = 0
    nasdaq = 0
    for i in stocks:
        exchange = i['exchangeShortName']
        if exchange == 'NYSE':
            nyse += 1
        elif exchange == 'NASDAQ':
            nasdaq += 1

    print(f'Total stocks returned: {len(stocks)}')
    print(f'Total NYSE:{nyse}')
    print(f'Total NASDAQ:{nasdaq}')

def test_get_live_qute():
    stock = Stock("META")
    r = stock.live_quote()
    percent_change = r[0]['changesPercentage']
    if percent_change >= 1.5:
        print(f'Volatile Day! {stock.ticker} moved {percent_change} percent!')
    else:
        print("Not Much Movement")
def test_volatility_builder():
    tickers = ["AAPL","META", "GOOG", "NFLX"]
    vol_per = [0.5, 1, 1.5, 2, 3]
    for f in vol_per:
        evaluation.volatility_builder(tickers, f)

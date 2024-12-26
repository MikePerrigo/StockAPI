import pytest
import pprint
from stocks import Stock
import stock_evaluation as evaluation


def test_valid_invalid_tickers():
    valid_stock = Stock("GOOG")
    with pytest.raises(ValueError):
        invalid_stock = Stock("Googling")

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
    assert stock_info[0]["symbol"] == ticker


def test_similar_return_sorting():
    stock = Stock("GOOG")
    r = stock.search()
    stocks = r.json()
    assert stocks[0]["exchangeShortName"] == "NASDAQ"
    nyse = 0
    nyse_tickers = []
    nasdaq = 0
    nasdaq_tickers = []
    for i in stocks:
        exchange = i['exchangeShortName']
        if exchange == 'NYSE':
            nyse_tickers.append(i["symbol"])
            nyse += 1
        elif exchange == 'NASDAQ':
            nasdaq_tickers.append(i["symbol"])
            nasdaq += 1
    assert stock.ticker in nasdaq_tickers

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

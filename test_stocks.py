import pytest
import pprint
from stocks import StockSearch

def test_search_fractyl():
    stock = StockSearch("GUTS")
    r = stock.search()
    stock_info = r.json()
    pprint.pprint(stock_info)
    assert stock_info[0]['stockExchange'] == 'Nasdaq'
    assert stock_info[0]['name'] == 'Fractyl Health, Inc. Common Stock'

@pytest.mark.parametrize("ticker", ["AAPL","META", "GOOG", "NFLX"])
def test_search_input(ticker):
    stock = StockSearch(ticker)
    r = stock.search()
    stock_info = r.json()
    pprint.pprint(stock_info[0])

def test_invalid_ticker():
    stock = StockSearch("GOOG")
    r = stock.search()
    stocks = r.json()
    nyse = 0
    nasdaq = 0
    total_stocks_found = len(stocks)
    for i in stocks:
        exchangde = i['exchangeShortName']
        if exchangde == 'NYSE':
            nyse += 1
        elif exchangde == 'NASDAQ':
            nasdaq += 1

    print(f'Total stocks returned: {len(stocks)}')
    print(f'Total NYSE:{nyse}')
    print(f'Total NASDAQ:{nasdaq}')





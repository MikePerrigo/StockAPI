import pytest
from stocks import Stock
import stock_evaluation as evaluation


def test_invalid_tickers():
    """
    Assert that an exception is raised when trying to search for a ticker that is not listed
    :return:
    """
    invalid_stock = Stock("Googling")
    with pytest.raises(ValueError):
        invalid_stock.search()

    valid_stock = Stock("GOOG")
    r = valid_stock.search()
    assert r.json() is not None, "Response is empty"


def test_search_google():
    """
    Assert that the returned info for the Google ticker is correct
    :return:
    """
    stock = Stock("GOOG")
    r = stock.search()
    stock_info = r.json()
    assert stock_info[0]['stockExchange'] == 'NASDAQ Global Select'
    assert stock_info[0]['name'] == 'Alphabet Inc.'

@pytest.mark.parametrize("ticker", ["AAPL","META", "GOOG", "NFLX"])
def test_search_input(ticker):
    """
    Asserts that searching for the ticker returns a matching "symbol" in the JSON
    :param ticker: The list of tickers to check
    :return:
    """
    stock = Stock(ticker)
    r = stock.search()
    stock_info = r.json()
    assert stock_info[0]["symbol"] == ticker


def test_similar_return_sorting():
    """
    Tests sorting through the pool of similar ticker symbols when searching for a given ticker.
    This sorts into NYSE and NASDAQ lists, the expected exchange is passed in with the ticker.
    :return:
    """
    stocks = {
        "stock_1": {
            "symbol": "GOOG",
            "exchange": "NASDAQ"
        },
        "stock_2": {
            "symbol": "GM",
            "exchange": "NYSE"
        }
    }
    keys = ["stock_1", "stock_2"]
    for i in keys:
        current = stocks[i]
        nyse_tickers, nasdaq_tickers = evaluation.exchange_sorter(current["symbol"], current["exchange"])
        if current["exchange"] == "NYSE":
            assert current["symbol"] in nyse_tickers
            print(nyse_tickers)
        elif current["exchange"] == "NASDAQ":
            assert current["symbol"] in nasdaq_tickers
            print(nasdaq_tickers)


def test_get_live_qute():
    """
    Informational test to call out if a ticker has moved a lot.
    :return:
    """
    stock = Stock("META")
    r = stock.live_quote()
    percent_change = r[0]['changesPercentage']
    if percent_change >= 1.5:
        print(f'Volatile Day! {stock.ticker} moved {percent_change} percent!')
    else:
        print("Not Much Movement")


def test_volatility_builder():
    """
    Tests the evaluation of the current days change percentage against the preset volatility.
    If the days change percentage is greater than the volatility, the stock should be evaluated for entry/exit
    :return:
    """
    tickers = ["AAPL","META", "GOOG", "NFLX"]
    volatility = 1.7
    evaluation_list = evaluation.volatility_builder(tickers, volatility)
    for ticker in tickers:
        eval = Stock(ticker)
        r = eval.live_quote()
        change_percentage = r[0]['changesPercentage']
        if abs(change_percentage) > volatility:
            assert eval.ticker in evaluation_list, f'Ticker {ticker} should be in evaluation list but is not'
    print(f'Stocks to evaluate { evaluation_list }')


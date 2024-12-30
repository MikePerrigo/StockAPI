from stocks import Stock


def volatility_builder(tickers=None, volatility: float = 1.25):
    # Declare stock so not referenced before assignment linting error
    stock = None
    evaluation_list = []
    for stock in tickers:
        stock = Stock(stock)
        r = stock.live_quote()
        if r[0]['changesPercentage'] >= volatility:
            evaluation_list.append(stock.ticker)
            print(f'Added {stock.ticker}')
        else:
            print(f'Not adding {stock.ticker}')
    print(f'Stocks to evaluate entry/exit: {evaluation_list}')

def exchange_sorter(ticker: str = None, exchange: str = None):
    stock = Stock(ticker)
    r = stock.search()
    stocks = r.json()
    assert stocks[0]["exchangeShortName"] == exchange
    nyse, nasdaq = 0, 0
    nyse_tickers, nasdaq_tickers = [], []
    for i in stocks:
        exchange = i['exchangeShortName']
        if exchange == 'NYSE':
            nyse_tickers.append(i["symbol"])
            nyse += 1
        elif exchange == 'NASDAQ':
            nasdaq_tickers.append(i["symbol"])
            nasdaq += 1
    return nyse_tickers, nasdaq_tickers
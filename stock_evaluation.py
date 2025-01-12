from stocks import Stock


def volatility_builder(tickers=None, volatility: float = 1.25):
    # Declare stock so not referenced before assignment linting error
    stock = None
    evaluation_list = []

    # Assess the stocks' current daily change amount.
    # If the current change percentage is greater than the volatility value, add to an evaluation list
    for stock in tickers:
        stock = Stock(stock)
        r = stock.live_quote()
        change_percentage = r[0]['changesPercentage']
        print(f'Ticker {stock.ticker} has moved {change_percentage}')
        if abs(r[0]['changesPercentage']) >= volatility:
            evaluation_list.append(stock.ticker)
            print(f'Added {stock.ticker}')
            print('------------')
        else:
            print(f'Not adding {stock.ticker}')
            print('------------')
    return evaluation_list


def exchange_sorter(ticker: str = None, exchange: str = None):
    """
    Each stock returns a large pool of similar stocks when using the stock.search() call
    This function sorts the pool of stocks into a list of either those on the NYSE or the NASDAQ
    :param ticker:
    :param exchange:
    :return:
    """
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
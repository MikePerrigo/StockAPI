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
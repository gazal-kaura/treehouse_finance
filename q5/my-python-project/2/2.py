from datetime import datetime, timedelta
from dateutil.relativedelta import *
import numpy as np
import pandas as pd
from pandas_datareader import data

#Returns Optimized Portfolio
def getOptimizedPortfolio(end, stocks, num_simulations):
    start = datetime.strftime(datetime.strptime(end, "%Y/%m/%d") - timedelta(days=252), "%Y/%m/%d")
    df = data.DataReader(stocks, 'yahoo', start=start, end=end)
    daily_returns = df['Close'].pct_change()
    mean_daily_returns = daily_returns.mean()
    cov_matrix = daily_returns.cov()
    results = np.zeros((4 + len(stocks) - 1, num_simulations))

    for i in range(num_simulations):
        weights = np.array(np.random.uniform(-1, 1, len(stocks)))
        weights /= np.sum(weights)

        portfolio_return = np.sum(mean_daily_returns * weights) * 252
        portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)

        results[0, i] = portfolio_return
        results[1, i] = portfolio_std_dev
        results[2, i] = results[0, i] / results[1, i]
        for j in range(len(weights)):
            results[j + 3, i] = weights[j]

    cols = ['ret', 'stdev', 'sharpe']
    cols.extend(stocks)
    results_frame = pd.DataFrame(results.T,
                                 columns=cols)
    max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]
    return max_sharpe_port[3:]

# Returns Sum
def sum(a,b):
    """
    Returns Sum
    :param a: number
    :param b: number
    :return: sum
    """
    return a+b

start = "2016/01/01"
start_date = datetime.strptime(start, "%Y/%m/%d")
result = {}
stocks = ['AAPL', 'IBM', 'GOOG', 'BP', 'XOM', 'COST', 'GS']
for i in range(12):
    end_date = start_date + relativedelta(months=+1) - relativedelta(days=1)
    start_date = start_date + relativedelta(months=+1)
    print("Running Portfolio Rebalancing at {}".format(datetime.strftime(end_date, "%Y/%m/%d")))
    portfolio = getOptimizedPortfolio(datetime.strftime(end_date, "%Y/%m/%d"), stocks, 25000)
    result[i+1] = dict(zip(stocks, portfolio.tolist()))

for k,v in result.items():
    print(k, ":", v)
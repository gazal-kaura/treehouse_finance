import numpy as np
from pandas_datareader import data


def getHistoricalVaRAndCVaR(df, weights, confidence_level):
    """
    This method computes VaR and CVaR using historical prices.
    :param df: Stocks Dataframe.
    :param weights: Weight allocation of each stock in the portfolio.
    :param confidence_level: Confidence level (1-100)
    :return: A Tuple (VaR, CVaR)
    """
    daily_returns = df['Close'].pct_change()
    daily_returns = daily_returns.dropna()
    daily_returns['portfolio'] = daily_returns.dot(weights)
    historicalVaR = abs(np.percentile(daily_returns['portfolio'], 100 - confidence_level))
    historicalCVaR = abs(daily_returns[daily_returns['portfolio'] <= historicalVaR]['portfolio'].mean())
    return historicalVaR * 100, historicalCVaR * 100


stocks = ['AAPL', 'IBM', 'GOOG', 'BP', 'XOM', 'COST', 'GS']
df = data.DataReader(stocks, 'yahoo', start='2016/01/01', end='2016/12/31')
weights = np.array([.15, .2, .2, .15, .1, 0.15, 0.05])
print(getHistoricalVaRAndCVaR(df, weights, 95))

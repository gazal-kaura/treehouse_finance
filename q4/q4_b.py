import numpy as np
from pandas_datareader import data
from scipy.stats import norm


def getParametricVaRAndCVaR(df, weights, confidence_level):
    daily_returns = df['Close'].pct_change()
    daily_returns = daily_returns.dropna()
    portfolio_ret = daily_returns.mean().dot(weights)
    portfolio_stdev = np.sqrt(weights.T.dot(daily_returns.cov()).dot(weights))
    VaR = norm.ppf(confidence_level) * portfolio_stdev - portfolio_ret
    CVaR = ((1 - confidence_level) ** -1) * norm.pdf(norm.ppf((1 - confidence_level))) * portfolio_stdev - portfolio_ret
    return VaR * 100, CVaR * 100


stocks = ['AAPL', 'IBM', 'GOOG', 'BP', 'XOM', 'COST', 'GS']
df = data.DataReader(stocks, 'yahoo', start='2016/01/01', end='2016/12/31')
weights = np.array([.15, .2, .2, .15, .1, 0.15, 0.05])
print(getParametricVaRAndCVaR(df, weights, 0.95))

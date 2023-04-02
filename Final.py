
# !pip install yfinance
# we install all the libraries we will use
import random
import yfinance as yf
import math
import numpy as np
import numpy.random as npr
from pylab import plt, mpl
import scipy.optimize as sco
import pandas as pd

#tickers list of the S&P 500 that we have found

tick = ['MMM', 'AOS', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADM', 'ADBE', 'ADP', 'AAP', 'AES', 'AFL', 'A', 'AIG', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AMD', 'AEE', 'AAL', 'AEP', 'AXP', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ANET', 'AIZ', 'T', 'ATO', 'ADSK', 'AZO', 'AVB', 'AVY', 'BKR', 'BALL', 'BAC', 'BBWI', 'BAX', 'BDX', 'WRB', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BK', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'CHRW', 'CDNS', 'CZR', 'CPT', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CDAY', 'CF', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'COO', 'CPRT', 'GLW', 'COST', 'CTRA', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DISH', 'DIS', 'DG', 'DLTR', 'D', 'DPZ', 'DOV','DTE', 'DUK', 'DD', 'DXC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ENPH', 'ETR', 'EOG', 'EPAM', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'RE', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FDS', 'FAST', 'FRT', 'FDX', 'FITB', 'FRC', 'FE', 'FIS', 'FISV', 'FLT', 'FMC', 'F', 'FTNT', 'FTV', 'BEN', 'FCX', 'AJG', 'GRMN', 'IT', 'GE', 'GNRC', 'GD', 'GIS', 'GPC', 'GILD', 'GL', 'GPN', 'GM', 'GS', 'GWW', 'HAL', 'HIG', 'HAS', 'HCA', 'PEAK', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUM', 'HII', 'HBAN', 'IEX', 'IDXX', 'ITW', 'ILMN', 'INCY', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JBHT', 'JKHY', 'J', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LDOS', 'LEN', 'LLY', 'LNC', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LUMN', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MHK', 'MOH', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NWL', 'NEM', 'NWSA', 'NWS', 'NEE', 'NKE', 'NI', 'NDSN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC', 'OKE', 'ORCL', 'PCAR', 'PKG', 'PARA', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PENN', 'PNR', 'PEP', 'PKI', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PTC', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SEE', 'SRE', 'NOW', 'SHW', 'SBNY', 'SPG', 'SWKS', 'SJM', 'SNA', 'SEDG', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STE', 'SYK', 'SIVB', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TRMB', 'TFC', 'TYL', 'TSN', 'USB', 'UDR', 'ULTA', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', 'UHS', 'VLO', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VFC', 'VTRS', 'V', 'VNO', 'VMC', 'WAB', 'WMT', 'WBA', 'WBD', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WRK', 'WY', 'WHR', 'WMB', 'WTW', 'WYNN', 'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS']


# This line can be used if you prefer to use a sample from the S&P500 ticker matrix. 
# Just replace the 200 with any number you want and the script will pick up the best tickers (number you define on line 53 by replacing the 5 with any number you want).
tick = random.sample(tick, 200)

# We have chosen a wide range, from 2010 to 2021 as the starting year, so the script cannot start in 2023 and end in 2025 otherwise it would make no sense
start_years = range(2010, 2021)
start_year = random.choice(start_years)
start_date = f"{start_year}-01-01"
#Below, we can change the +2 by any other number as long as we replace the 2021 on lines 36 and 113. if we put +5, we should then put 2018 as a limit
end_date = f"{start_year+2}-01-01"

data = yf.download(tickers=tick, start=start_date, end=end_date, interval="1d")['Adj Close']

# We calculate the daily returns for each ticker

returns = data.pct_change()

# We calculate total returns for each ticker

total_returns = (1 + returns).prod() - 1

# We select the tickers with the best returns. the [:10] means 

top_tickers = total_returns.sort_values(ascending=False)[:10].index

# We set up a table with the returns of the best tickers

top_tickers_list = list(total_returns[top_tickers].index)

# Let's change the nomenclature because it is shorter hence better

symbols = top_tickers_list

# We download the data of the tickers drawn

data = yf.download(tickers=symbols, start="2010-01-01", end="2018-06-29")['Adj Close']

# We are re-calculating stock returns because they are not kept in memory

noa = len(symbols)

# Log returns of the stocks. We divide each element by its previous element using data.shift(1)
rets = np.log(data / data.shift(1))

# We calculate the annualized mean of the assets
rets.mean() * 252

# We calculate the annualized covariance matrix of the assets
rets.cov() * 252

# Calculate random weights for each stock

weights = np.random.random(noa)
weights /= np.sum(weights)

#Annualized portfolio return given the portfolio weights.

np.sum(rets.mean() * weights) * 252

#Annualized portfolio variance given the portfolio weight

np.dot(weights.T, np.dot(rets.cov() * 252, weights))

#Here is the annualized portfolio return by computing the weighted mean return and the square root of the weighted covariance matrix, respectively.

math.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))

def port_ret(weights):
    return np.sum(rets.mean() * weights) * 252

def port_vol(weights):
    return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))

#We now want the most interesting portfolio so we run 100 simulations, then we take the best combination.
num_simulations =100
best_weights = np.zeros(noa)
max_sharpe_ratio = -1
max_return = -1

for i in range(num_simulations):
    weights = np.random.random(noa)
    weights /= np.sum(weights)

    portfolio_return = np.sum(rets.mean() * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))

    sharpe_ratio = portfolio_return / portfolio_std_dev

    if sharpe_ratio > max_sharpe_ratio:
        max_sharpe_ratio = sharpe_ratio
        best_weights = weights
        max_return = portfolio_return
        
print(f"The most efficient stocks with the most efficient weights according to the {num_simulations} trials done for the years {start_year} to {start_year+2} are:")
for i in range(len(symbols)):
    print(f"{symbols[i]}: {best_weights[i]*100:.2f}%")
print (f"With this portfolio we can obtain a maximum return of {max_return*100:.2f}% ")
print(" And we also have a maximum Sharpe Ratio of", max_sharpe_ratio)

#Monte Carlo simulation of portfolio weights for the plot

prets = []
pvols = []
for p in range (2500*noa):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(port_ret(weights))
    pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)

# We create a scatter plot with a cool/warm map that represents the sharpe ratio.
# x-axis shows the volatility and y-axis shows the expected return
plt.figure(figsize=(10, 6))
plt.scatter(pvols, prets, c=prets / pvols,
marker='o', cmap='coolwarm')
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio');

# defining the minimizing function in order to get the best sharpe
def min_func_sharpe(weights):
    return -port_ret(weights) / port_vol(weights)

#We make sure that the portfolio weights are equal to 1 or 100%
cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

#input of the parameter
bnds = tuple((0, 1) for x in range(noa))

#defining the equal weight vector
eweights = np.array(noa * [1. / noa,])
eweights

min_func_sharpe(eweights)

# we minimize the process with sco.minimize
opts = sco.minimize(min_func_sharpe, eweights,
# We use the SLSQP method. This moethod works effectively for issues with changeable boundaries, as well as linear and nonlinear restrictions.
method='SLSQP', bounds=bnds,constraints=cons)

# optimal portfolio weights with 3 rounding digits
opts['x'].round(3)

#return results
port_ret(opts['x']).round(3)
#volatility results
port_vol(opts['x']).round(3)
#the maximum sharpe ratio
port_ret(opts['x']) / port_vol(opts['x'])

df = pd.DataFrame(opts['x'],
index=[top_tickers_list])
df
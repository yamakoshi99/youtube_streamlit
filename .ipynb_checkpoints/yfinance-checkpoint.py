import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

%matplotlib inline

aaple = yf.Ticker('AAPL')
aaple.historu()
yfinance.Ticker object <AAPL>

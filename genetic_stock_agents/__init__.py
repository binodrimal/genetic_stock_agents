import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from datetime import date
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yfinance'])
import yfinance as yf
from scipy import stats

ticker = list(pd.read_csv('https://github.com/datasets/s-and-p-500-companies/raw/master/data/constituents.csv')['Symbol'])

def get_data(tickers, begin_date=None,end_date=None,window=None):
  """
    data access for given tickers from begin_date to end_date 
    in the interval of given window such as '15min',...,'1h'.
    tickers: stock symbols
  """
  df = yf.download(tickers, start = begin_date,
                     auto_adjust=True,#only download adjusted data
                     end= end_date, interval = window)
  #df = yf.download(tickers, period='1d', interval='1d') 
  return df

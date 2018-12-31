from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import numpy as np

class TickerHistory(object):

    def __init__(self, ticker='', start_date='2000-09-24', stop_date = '2018-09-24'):
        self.data = pdr.get_data_yahoo(ticker, start_date, stop_date)
        self.np_data = self.data.values
        self.highs = self.np_data[:,0]
        self.lows = self.np_data[:,1]
        self.opening = self.np_data[:,2]
        self.closing = self.np_data[:,3]
        self.volume = self.np_data[:,4]
        self.adj_close = self.np_data[:,5]

class TraderBot(object):

    def __init__(self, name=None, tickers=None, init_capitol=25000, init_portfolio=None):
        self.name = name
        self.tickers = tickers
        self.ticker_history = {}
        self.capitol = init_capitol
        self.value = init_capitol
        if init_portfolio == None:
            self.portfolio = {}

    def add_new_data(self, data):
        pass

    def buy_stock(self, ticker, cost, number):
        if self.capitol >= cost*number:
            if ticker in self.portfolio:
                self.portfolio[ticker] = number + self.portfolio[ticker]
            else:
                self.portfolio[ticker] = number
            self.capitol -= cost*number
            return True
        else:
            return False
        
    def sell_stock(self, ticker, cost, number):

        if (ticker in self.portfolio) and (self.portfolio[ticker] >= number):
            self.portfolio[ticker] = self.portfolio[ticker] - number
            self.capitol += cost*number
            return True
        else:
            return False

    def run_simulation(self, start_date, stop_date):
        dummy_data = pdr.get_data_yahoo('SPY', start_date, stop_date)
        dummy_data = dummy_data.values
        days = len(dummy_data[:,0])
        day_list = np.linspace(0, days - 1, days)
        for ticker in self.tickers:
            self.ticker_history[ticker] = TickerHistory(ticker)
        for day in day_list:
            day = int(day)
            self.the_algorithm(day)
            self.value = self.update_value(day)

    def the_algorithm(self, day):
        pass

    def update_value(self, day):
        stock_value = 0
        for ticker in self.portfolio:
            cost = self.ticker_history[ticker].highs[day]
            stock_value += self.portfolio[ticker]*cost
        return stock_value + self.capitol
            

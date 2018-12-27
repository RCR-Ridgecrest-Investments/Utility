from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import numpy as np


class TraderBot(object):

    def __init__(self, name=None, tickers=None, init_capitol=25000, init_portfolio=None):
        self.name = name
        self.tickers = tickers
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

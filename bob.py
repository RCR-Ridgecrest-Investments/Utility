from Utility.traderbot import TraderBot

class Bob(TraderBot):

    def the_algorithm(self, day):
        for ticker in self.tickers:
            if day > 0:
                cost = self.ticker_history[ticker].opening[day]
                prev_cost = self.ticker_history[ticker].closing[day - 1]
                if prev_cost < cost:
                    self.buy_stock(ticker, cost, 1)
                else:
                    self.sell_stock(ticker, cost, 1)

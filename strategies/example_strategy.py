import backtrader as bt

class Strategy(bt.Strategy):
    params = ("ma_period", 20),

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.p.ma_period)

    def next(self):
        if not self.position:
            if self.datas[0].close[0] > self.sma[0]:
                self.buy()
        else:
            if self.datas[0].close[0] < self.sma[0]:
                self.sell()
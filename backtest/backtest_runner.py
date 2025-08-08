import yfinance as yf
import backtrader as bt
import os
import importlib

def run_backtest(strategy_cls, ticker, start, end, cash=10000):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy_cls)

    data = bt.feeds.PandasData(dataname=yf.download(ticker, start=start, end=end))
    cerebro.adddata(data)
    cerebro.broker.set_cash(cash)
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue():.2f}")
    cerebro.run()
    print(f"Final Portfolio Value: {cerebro.broker.getvalue():.2f}")
    cerebro.plot()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", type=str, required=True, help="Nom du fichier de la stratégie sans .py")
    parser.add_argument("--ticker", type=str, default="AAPL")
    parser.add_argument("--start", type=str, default="2022-01-01")
    parser.add_argument("--end", type=str, default="2023-01-01")
    args = parser.parse_args()

    strategy_module = importlib.import_module(f"strategies.{args.strategy}")
    strategy_cls = getattr(strategy_module, "Strategy")
    run_backtest(strategy_cls, args.ticker, args.start, args.end)
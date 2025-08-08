import yfinance as yf
import pandas as pd

def fetch_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv(f"data/{ticker}_{start}_{end}.csv")
    return df

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", type=str, required=True)
    parser.add_argument("--start", type=str, required=True)
    parser.add_argument("--end", type=str, required=True)
    args = parser.parse_args()
    fetch_data(args.ticker, args.start, args.end)
import json
import os

WATCHLIST_FILE = "watchlist.json"


def load_watchlist():
    if not os.path.exists(WATCHLIST_FILE):
        return []
    with open(WATCHLIST_FILE, "r") as f:
        return json.load(f)


def save_watchlist(tickers):
    with open(WATCHLIST_FILE, "w") as f:
        json.dump(tickers, f)


def add_to_watchlist(ticker):
    tickers = load_watchlist()
    ticker = ticker.upper()
    if ticker not in tickers:
        tickers.append(ticker)
        save_watchlist(tickers)
    return tickers


def remove_from_watchlist(ticker):
    tickers = load_watchlist()
    ticker = ticker.upper()
    if ticker in tickers:
        tickers.remove(ticker)
        save_watchlist(tickers)
    return tickers

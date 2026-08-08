import yfinance as yf

def get_company_data(ticker_symbol):
    company = yf.Ticker(ticker_symbol)
    info = company.info

    data = {
        "name": info.get("longName"),
        "current_price": info.get("currentPrice"),
        "debt_to_equity": info.get("debtToEquity"),
        "revenue_growth": info.get("revenueGrowth"),
        "market_cap": info.get("marketCap"),
    }

    return data


if __name__ == "__main__":
    result = get_company_data("AAPL")
    print(result)


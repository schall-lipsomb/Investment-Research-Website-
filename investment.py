import yfinance as yf

def get_company_data(ticker_symbol):
    company = yf.Ticker(ticker_symbol)
    info = company.info

    price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")

    data = {
        "ticker": ticker_symbol.upper(),
        "name": info.get("longName") or info.get("shortName"),
        "current_price": price,
        "debt_to_equity": info.get("debtToEquity"),
        "revenue_growth": format_percent(info.get("revenueGrowth")),
        "revenue_growth_raw": info.get("revenueGrowth"),
        "market_cap": format_large_number(info.get("marketCap")),
    }

    return data


def format_percent(value):
    if value is None:
        return "N/A"
    return f"{value * 100:.1f}%"


def format_large_number(value):
    if value is None:
        return "N/A"
    if value >= 1_000_000_000_000:
        return f"${value / 1_000_000_000_000:.2f}T"
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    return f"${value:,.0f}"


def get_price_history(ticker_symbol, period="6mo"):
    company = yf.Ticker(ticker_symbol)
    hist = company.history(period=period)

    dates = hist.index.strftime("%Y-%m-%d").tolist()
    prices = hist["Close"].round(2).tolist()

    return {"dates": dates, "prices": prices}


def get_revenue_history(ticker_symbol):
    company = yf.Ticker(ticker_symbol)
    financials = company.financials
    revenue = financials.loc["Total Revenue"]

    years = revenue.index.strftime("%Y").tolist()
    values = revenue.tolist()

    paired = [(y, v) for y, v in zip(years, values) if v == v]

    paired.reverse()
    years = [p[0] for p in paired]
    values = [p[1] for p in paired]

    return {"years": years, "revenue": values}


if __name__ == "__main__":
    result = get_company_data("AAPL")
    print(result)

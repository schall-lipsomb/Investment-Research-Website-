from flask import Flask, render_template, redirect, url_for, jsonify, request
from investment import get_company_data, get_price_history, get_revenue_history
from watchlist import load_watchlist, add_to_watchlist, remove_from_watchlist
from risk_model import predict_risk

app = Flask(__name__)

@app.route("/")
def home():
    tickers = load_watchlist()
    companies = [get_company_data(t) for t in tickers]
    return render_template("home.html", companies=companies)

@app.route("/search")
def search():
    ticker = request.args.get("ticker", "").strip().upper()
    if not ticker:
        return redirect(url_for("home"))
    return redirect(url_for("company_profile", ticker=ticker))

@app.route("/company/<ticker>")
def company_profile(ticker):
    company = get_company_data(ticker)
    watchlist = load_watchlist()
    is_watched = ticker.upper() in watchlist
    risk = predict_risk(company["debt_to_equity"], company["revenue_growth_raw"])
    return render_template("company.html", company=company, ticker=ticker, is_watched=is_watched, risk=risk)

@app.route("/watchlist/add/<ticker>")
def add_watch(ticker):
    add_to_watchlist(ticker)
    return redirect(url_for("company_profile", ticker=ticker))

@app.route("/watchlist/remove/<ticker>")
def remove_watch(ticker):
    remove_from_watchlist(ticker)
    return redirect(url_for("company_profile", ticker=ticker))

@app.route("/api/history/<ticker>")
def price_history_api(ticker):
    history = get_price_history(ticker)
    return jsonify(history)

@app.route("/api/revenue/<ticker>")
def revenue_history_api(ticker):
    revenue = get_revenue_history(ticker)
    return jsonify(revenue)

if __name__ == "__main__":
    app.run(debug=True)

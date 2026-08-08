from flask import Flask, render_template
from investment import get_company_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/company/<ticker>")
def company_profile(ticker):
    company = get_company_data(ticker)
    return render_template("company.html", company=company)

if __name__ == "__main__":
    app.run(debug=True)

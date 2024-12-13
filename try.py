import yfinance as yf

def fetch_stock_data(stock_symbol, start_date, end_date):
    stock = yf.Ticker(stock_symbol)
    return stock.history(start=start_date, end=end_date)

# Example Usage
stock_data = fetch_stock_data("RELIANCE.NS", "2024-12-01", "2024-12-14")
print(stock_data)
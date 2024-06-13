import yfinance as yf

class Stock:
    def __init__(self, ticker, shares):
        self.ticker = ticker
        self.shares = shares
        self.data = yf.Ticker(ticker).history(period="1d")
        self.price = self.data['Close'][0]

    def get_value(self):
        return self.shares * self.price

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def portfolio_value(self):
        total_value = 0
        for stock in self.stocks:
            total_value += stock.get_value()
        return total_value

    def show_portfolio(self):
        for stock in self.stocks:
            print(f"{stock.ticker}: {stock.shares} shares, Current Price: ${stock.price}, Total Value: ${stock.get_value()}")

# Example Usage
if __name__ == "__main__":
    portfolio = Portfolio()
    stock1 = Stock("AAPL", 10)
    stock2 = Stock("MSFT", 5)
    portfolio.add_stock(stock1)
    portfolio.add_stock(stock2)
    print("Portfolio Value:", portfolio.portfolio_value())
    portfolio.show_portfolio()
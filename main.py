"""
Main entry point for portfolio management demo.
"""
from src.entities.stock import Stock
from src.entities.portfolio import Portfolio

def main() -> None:
    meta = Stock('META', 'Meta Platforms Inc.')
    aapl = Stock('AAPL', 'Apple Inc.')
    holdings = {
        'META': (meta, 10),
        'AAPL': (aapl, 10)
    }
    allocation = {
        'META': 0.4,
        'AAPL': 0.6
    }
    portfolio = Portfolio(holdings, allocation)
    print("Total portfolio value:", portfolio.total_value())
    print("Rebalance actions:", portfolio.rebalance())

if __name__ == "__main__":
    main()

"""
Stock entity representing a financial asset in the portfolio.
"""
from typing import Optional

class Stock:
    def __init__(self, symbol: str, name: str):
        """
        Args:
            symbol (str): Ticker symbol of the stock (e.g., 'META', 'AAPL').
            name (str): Full name of the stock/company.
        """
        self.symbol = symbol
        self.name = name

    def get_current_price(self) -> Optional[float]:
        """
        Returns the last available price for the stock.
        In a real scenario, this would fetch data from an API.
        Here, it returns a mock value for demonstration.
        """
        mock_prices = {
            'META': 350.0,
            'AAPL': 180.0,
        }
        return mock_prices.get(self.symbol)

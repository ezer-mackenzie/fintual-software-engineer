"""
Portfolio entity representing a collection of stocks and their allocations.
"""
from typing import Dict, Tuple
from .stock import Stock

class Portfolio:
    def __init__(self, holdings: Dict[str, Tuple[Stock, int]], allocation: Dict[str, float]):
        """
        Args:
            holdings (Dict[str, Tuple[Stock, int]]): Current stocks in portfolio with their quantities.
            allocation (Dict[str, float]): Target allocation percentages per stock symbol (e.g., {'META': 0.4, 'AAPL': 0.6}).
        """
        self.holdings = holdings
        self.allocation = allocation

    def total_value(self) -> float:
        """
        Calculates the total value of the portfolio based on current prices.
        """
        return sum(stock.get_current_price() * qty for stock, qty in self.holdings.values())

    def rebalance(self) -> Dict[str, Dict[str, float]]:
        """
        Determines buy/sell actions to achieve target allocation.
        Truncates results to 11 decimals (no rounding).
        Returns:
            Dict[str, Dict[str, float]]: Actions per stock symbol, e.g., {'META': {'buy': 10, 'sell': 0}}
        """
        def truncate(num: float, decimals: int = 11) -> float:
            if num >= 0:
                return float(str(num)[:str(num).find('.') + decimals + 1]) if '.' in str(num) else float(num)
            else:
                s = str(num)
                return float(s[:s.find('.') + decimals + 1]) if '.' in s else float(num)

        actions = {}
        total_val = self.total_value()
        for symbol, (stock, qty) in self.holdings.items():
            current_val = stock.get_current_price() * qty
            target_val = self.allocation.get(symbol, 0) * total_val
            diff = target_val - current_val
            price = stock.get_current_price()
            if price:
                if diff > 0:
                    buy = truncate(diff / price)
                    actions[symbol] = {'buy': buy, 'sell': 0.0}
                elif diff < 0:
                    sell = truncate(-diff / price)
                    actions[symbol] = {'buy': 0.0, 'sell': sell}
                else:
                    actions[symbol] = {'buy': 0.0, 'sell': 0.0}
        return actions

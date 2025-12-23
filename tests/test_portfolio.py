"""
Unit tests for Portfolio and rebalance logic.
"""
import unittest
from src.entities.stock import Stock
from src.entities.portfolio import Portfolio

class TestPortfolio(unittest.TestCase):
    def setUp(self) -> None:
        self.meta = Stock('META', 'Meta Platforms Inc.')
        self.aapl = Stock('AAPL', 'Apple Inc.')
        holdings = {
            'META': (self.meta, 10),
            'AAPL': (self.aapl, 10)
        }
        allocation = {
            'META': 0.4,
            'AAPL': 0.6
        }
        self.portfolio = Portfolio(holdings, allocation)

    def test_total_value(self) -> None:
        total = self.portfolio.total_value()
        self.assertAlmostEqual(total, 350.0*10 + 180.0*10)


    def test_rebalance(self) -> None:
        actions = self.portfolio.rebalance()
        self.assertIn('META', actions)
        self.assertIn('AAPL', actions)
        # Check that buy/sell values are numeric (float or int)
        self.assertIsInstance(actions['META']['buy'], (float, int))
        self.assertIsInstance(actions['AAPL']['sell'], (float, int))
        # Check that buy/sell are >= 0
        for symbol in actions:
            self.assertGreaterEqual(actions[symbol]['buy'], 0)
            self.assertGreaterEqual(actions[symbol]['sell'], 0)

    def test_rebalance_no_action_needed(self):
        # Portfolio already matches allocation
        meta = Stock('META', 'Meta Platforms Inc.')
        aapl = Stock('AAPL', 'Apple Inc.')
        holdings = {
            'META': (meta, 7),
            'AAPL': (aapl, 14)
        }
        allocation = {
            'META': 0.5,
            'AAPL': 0.5
        }
        portfolio = Portfolio(holdings, allocation)
        actions = portfolio.rebalance()
        for symbol in actions:
            self.assertAlmostEqual(actions[symbol]['buy'], 0, delta=0.2)
            self.assertAlmostEqual(actions[symbol]['sell'], 0, delta=0.2)

    def test_rebalance_exceeds_tolerance(self) -> None:
        # Caso donde la diferencia supera el límite de tolerancia (0.2)
        meta = Stock('META', 'Meta Platforms Inc.')
        aapl = Stock('AAPL', 'Apple Inc.')
        holdings = {
            'META': (meta, 1),
            'AAPL': (aapl, 1)
        }
        allocation = {
            'META': 0.99,
            'AAPL': 0.01
        }
        portfolio = Portfolio(holdings, allocation)
        actions = portfolio.rebalance()
        # Al menos una acción debe superar la tolerancia
        with self.assertRaises(AssertionError):
            for symbol in actions:
                self.assertAlmostEqual(actions[symbol]['buy'], 0, delta=0.2)
                self.assertAlmostEqual(actions[symbol]['sell'], 0, delta=0.2)

    def test_rebalance_with_zero_holdings(self) -> None:
        # Portfolio with zero holdings for a stock
        meta = Stock('META', 'Meta Platforms Inc.')
        aapl = Stock('AAPL', 'Apple Inc.')
        holdings = {
            'META': (meta, 0),
            'AAPL': (aapl, 10)
        }
        allocation = {
            'META': 0.5,
            'AAPL': 0.5
        }
        portfolio = Portfolio(holdings, allocation)
        actions = portfolio.rebalance()
        self.assertGreater(actions['META']['buy'], 0)
        self.assertEqual(actions['META']['sell'], 0)
        self.assertEqual(actions['AAPL']['buy'], 0)

if __name__ == '__main__':
    unittest.main()

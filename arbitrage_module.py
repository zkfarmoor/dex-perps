# arbitrage_module.py
import time
import logging
from utilities import safe_execute

class PerpetualArbitrageModule:
    def __init__(self, client1, client2, threshold, max_exposure):
        self.client1 = client1
        self.client2 = client2
        self.threshold = threshold
        self.max_exposure = max_exposure

    @safe_execute
    def run(self):
        while True:
            book1 = self.client1.get_orderbook()
            book2 = self.client2.get_orderbook()
            best_ask1 = min(book1['asks'], key=lambda x: x['price'])
            best_bid2 = max(book2['bids'], key=lambda x: x['price'])

            if best_ask1['price'] < best_bid2['price']:
                profit = best_bid2['price'] - best_ask1['price'] - (best_ask1['price'] * 0.001 + best_bid2['price'] * 0.001)
                if profit > self.threshold:
                    size = min(best_ask1['size'], best_bid2['size'])
                    self.client1.execute_trade('sell', size, best_ask1['price'])
                    self.client2.execute_trade('buy', size, best_bid2['price'])
                    logging.info(f"Arbitrage executed: Sell {size} at {best_ask1['price']}, Buy {size} at {best_bid2['price']}")
            time.sleep(1)

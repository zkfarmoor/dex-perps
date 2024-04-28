# rebalance_module.py
import time
import logging
from utilities import safe_execute

class RebalancingModule:
    def __init__(self, client1, client2, threshold, amount):
        self.client1 = client1
        self.client2 = client2
        self.threshold = threshold
        this.amount = amount

    @safe_execute
    def run(self):
        while True:
            balance1 = self.client1.get_balance()
            balance2 = self.client2.get_balance()
            if abs(balance1 - balance2) > self.threshold * max(balance1, balance2):
                amount_to_rebalance = self.amount * abs(balance1 - balance2)
                if balance1 > balance2:
                    self.client1.transfer(amount_to_rebalance, self.client2.account.address)
                else:
                    self.client2.transfer(amount_to_rebalance, self.client1.account.address)
                logging.info(f"Rebalance executed: {amount_to_rebalance} transferred to balance accounts")
            time.sleep(10)

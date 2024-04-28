# delta_neutral_module.py
import time
import logging
from utilities import safe_execute

class DeltaNeutralVolumeModule:
    def __init__(self, client1, client2, max_exposure):
        self.client1 = client1
        self.client2 = client2
        self.max_exposure = max_exposure

    @safe_execute
    def run(self):
        while True:
            funding_rate1 = self.client1.get_funding_rate()
            funding_rate2 = self.client2.get_funding_rate()

            if abs(funding_rate1 - funding_rate2) > 0.0005:
                trade_size = 1000
                if funding_rate1 > funding_rate2:
                    self.client1.execute_trade('sell', trade_size, None)
                    self.client2.execute_trade('buy', trade_size, None)
                else:
                    self.client1.execute_trade('buy', trade_size, None)
                    self.client2.execute_trade('sell', trade_size, None)
                logging.info("Delta neutral strategy executed")
            time.sleep(1)

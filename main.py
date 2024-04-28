# main.py
import logging
from threading import Thread
from config_parser import parse_arguments
from exchange_client import ExchangeClient
from arbitrage_module import PerpetualArbitrageModule
from delta_neutral_module import DeltaNeutralVolumeModule
from rebalance_module import RebalancingModule
from utilities import setup_logging

def main():
    args = parse_arguments()
    setup_logging(args.log_level)

    # Initialize clients for Hyperliquid and Orderly
    client1 = ExchangeClient("https://api.hyperliquid.com", args.api_key_hyperliquid, args.wallet_address, args.private_key)
    client2 = ExchangeClient("https://api.orderly.network", args.api_key_orderly, args.wallet_address, args.private_key)

    # Initialize strategy modules with dynamic settings
    arb_module = PerpetualArbitrageModule(client1, client2, args.arb_threshold, args.arb_max_exposure)
    delta_module = DeltaNeutralVolumeModule(client1, client2, args.delta_max_exposure)
    rebalance_module = RebalancingModule(client1, client2, args.rebalance_threshold, args.rebalance_amount)

    # Start each strategy module in a separate thread for concurrent execution
    Thread(target=arb_module.run).start()
    Thread(target=delta_module.run).start()
    Thread(target=rebalance_module.run).start()

if __name__ == "__main__":
    main()

# config_parser.py
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Trading Bot Configuration")
    parser.add_argument("--api_key_hyperliquid", required=True, help="API key for Hyperliquid")
    parser.add_argument("--api_key_orderly", required=True, help="API key for Orderly")
    parser.add_argument("--wallet_address", required=True, help="Wallet address for transactions")
    parser.add_argument("--private_key", required=True, help="Private key for signing transactions")
    parser.add_argument("--arb_threshold", type=float, default=0.0025, help="Profit threshold for arbitrage")
    parser.add_argument("--arb_max_exposure", type=float, default=0.5, help="Max exposure for arbitrage trades")
    parser.add_argument("--delta_max_exposure", type=float, default=0.25, help="Max exposure for delta neutral trades")
    parser.add_argument("--rebalance_threshold", type=float, default=0.1, help="Threshold for rebalancing between exchanges")
    parser.add_argument("--rebalance_amount", type=float, default=0.05, help="Amount to rebalance between exchanges")
    parser.add_argument("--log_level", type=str, default="INFO", help="Logging level")
    return parser.parse_args()

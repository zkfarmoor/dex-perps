# config_parser.py
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Trading Bot Configuration")
    parser.add_argument("--api_key_hyperliquid", type=str, required=True, help="API key for Hyperliquid")
    parser.add_argument("--api_key_orderly", type=str, required=True, help="API key for Orderly")
    parser.add_argument("--wallet_address", type=str, required=True, help="Wallet address for transactions")
    parser.add_argument("--private_key", type=str, required=True, help="Private key for signing transactions")
    parser.add_argument("--arb_threshold", type=float, default=0.0025, help="Profit threshold for arbitrage (default: 0.0025)")
    parser.add_argument("--arb_max_exposure", type=float, default=0.5, help="Max exposure for arbitrage trades as a fraction of total capital (default: 0.5)")
    parser.add_argument("--delta_max_exposure", type=float, default=0.25, help="Max exposure for delta neutral trades as a fraction of total capital (default: 0.25)")
    parser.add_argument("--rebalance_threshold", type=float, default=0.1, help="Threshold for rebalancing between exchanges as a fraction of total capital (default: 0.1)")
    parser.add_argument("--rebalance_amount", type=float, default=0.05, help="Fraction of the difference to rebalance between exchanges (default: 0.05)")
    parser.add_argument("--log_level", type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default="INFO", help="Logging level")
    return parser.parse_args()

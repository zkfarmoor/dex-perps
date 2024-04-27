# file: trading_bot.py

import requests
import time
import threading
import json
from config import API_URL_HYPER, API_URL_ORDERLY, API_KEY_HYPER, API_KEY_ORDERLY

def get_headers(api_key):
    return {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

def load_settings():
    with open('settings.json', 'r') as f:
        return json.load(f)

def fetch_trading_pairs(api_url, api_key):
    response = requests.get(f"{api_url}/markets", headers=get_headers(api_key))
    response.raise_for_status()
    markets_data = response.json()
    return [market['symbol'] for market in markets_data]

def fetch_order_book(api_url, symbol, api_key):
    url = f"{api_url}/orderbook?symbol={symbol}"
    response = requests.get(url, headers=get_headers(api_key))
    return response.json()

def execute_trade(api_url, trade_type, symbol, quantity, api_key):
    url = f"{api_url}/trade"
    data = {'type': trade_type, 'symbol': symbol, 'quantity': quantity}
    response = requests.post(url, json=data, headers=get_headers(api_key))
    return response.json()

def fetch_balance(api_url, api_key):
    url = f"{api_url}/account/balance"
    response = requests.get(url, headers=get_headers(api_key))
    return response.json()['balance']

def transfer_funds(source_url, target_url, amount, source_api_key):
    # Placeholder for the transfer function, replace with actual API calls
    print(f"Transferred {amount} from {source_url} to {target_url}")

def rebalance_accounts():
    settings = load_settings()
    balance_hyper = fetch_balance(API_URL_HYPER, API_KEY_HYPER)
    balance_orderly = fetch_balance(API_URL_ORDERLY, API_KEY_ORDERLY)
    total_balance = balance_hyper + balance_orderly
    balance_diff = abs(balance_hyper - balance_orderly)

    max_diff_allowed = total_balance * (settings['rebalancing']['max_balance_difference_percent'] / 100)
    if balance_diff > max_diff_allowed:
        transfer_amount = total_balance * (settings['rebalancing']['transfer_percentage'] / 100)
        if balance_hyper > balance_orderly:
            transfer_funds(API_URL_HYPER, API_URL_ORDERLY, transfer_amount, API_KEY_HYPER)
        else:
            transfer_funds(API_URL_ORDERLY, API_URL_HYPER, transfer_amount, API_KEY_ORDERLY)
        print(f"Rebalanced {transfer_amount} between exchanges.")

def main():
    threading.Thread(target=rebalance_accounts).start()

if __name__ == "__main__":
    main()

# exchange_client.py
import requests
from web3 import Web3

class ExchangeClient:
    def __init__(self, base_url, api_key, wallet_address, private_key):
        self.base_url = base_url
        self.api_key = api_key
        self.web3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc'))
        self.account = self.web3.eth.account.privateKeyToAccount(private_key)

    def get_orderbook(self):
        return requests.get(f"{self.base_url}/orderbook", headers={"Authorization": f"Bearer {self.api_key}"}).json()

    def execute_trade(self, trade_type, size, price):
        trade_data = {'type': trade_type, 'size': size, 'price': price}
        response = requests.post(f"{self.base_url}/trade", json=trade_data, headers={"Authorization": f"Bearer {self.api_key}"})
        return response.json()

    def get_balance(self):
        contract = self.web3.eth.contract(address=self.account.address, abi=[])  # Placeholder ABI
        return contract.functions.getBalance().call()

    def transfer(self, amount, to_address):
        transaction = {
            'to': to_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 200000,
            'gasPrice': self.web3.toWei('10', 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(self.account.address)
        }
        signed_txn = self.account.sign_transaction(transaction)
        self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)

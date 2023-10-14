import datetime
import json
import random
import time

from eth_utils import to_checksum_address
from web3 import Web3

from config import NETWORKS, SETTINGS
from utils import fetch_price_from_coin_gecko


class BulkChecker(object):
    network_name = None
    web3: Web3 = None
    erc20_abi: str = None
    ether_price: int = None

    def __init__(self, network_name: str):
        self.network_name = network_name
        self.web3 = Web3(Web3.HTTPProvider(NETWORKS[network_name]['rpc']))
        self.erc20_abi = json.load(open("erc20_abi.json"))
        self.ether_price = fetch_price_from_coin_gecko()

    def bulk_check(self):
        csv_content = self.get_header()

        with open(SETTINGS['accounts_file']) as f:
            accounts = f.readlines()

        for account_address in accounts:
            if account_address != '\n':
                account_address = to_checksum_address(account_address.rstrip())
                print(f'fetching balances for {account_address}..')
                csv_content += account_address + ',' + self.get_account_balances(account_address=account_address)
                time.sleep(random.randint(SETTINGS['sleep_time']['min'], SETTINGS['sleep_time']['max']))
            else:
                csv_content += '\n'
        self.save_output(content=csv_content)

    def check_ether_balance(self, account_address: str):
        wei_amount = self.web3.eth.get_balance(to_checksum_address(account_address))
        return self.web3.from_wei(wei_amount, 'ether')

    def get_account_balances(self, account_address: str):
        tokens = NETWORKS[self.network_name]['tokens']
        account_balances = ''
        for ticker, token_address in tokens.items():
            if ticker == 'ETH':
                ether_balance = self.check_ether_balance(account_address=account_address)
                ether_balance_usd = round(self.ether_price * ether_balance, SETTINGS['usd_round'])
                ether_balance = round(ether_balance, SETTINGS['round'])
                account_balances += str(ether_balance) + ',' + str(ether_balance_usd) + ','
            else:
                token_contract = self.web3.eth.contract(address=to_checksum_address(token_address), abi=self.erc20_abi)
                token_balance = token_contract.functions.balanceOf(account_address).call()
                token_decimals = token_contract.functions.decimals().call()
                token_balance /= 10 ** token_decimals
                token_balance = round(token_balance, SETTINGS['round'])
                account_balances += str(token_balance) + ','
        return account_balances[:-1] + '\n'

    def get_header(self):
        tokens = NETWORKS[self.network_name]['tokens']
        header = 'account,'
        for ticker in tokens:
            if ticker == 'ETH':
                header += 'ETH,ETH(USD),'
            else:
                header += ticker + ','
        return header[:-1] + '\n'

    def save_output(self, content):
        actual_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f'{self.network_name}_{actual_datetime}_balances.csv'
        f = open(output_filename, "w")
        f.write(content)
        f.close()
        print(f'Output saved to {output_filename}')


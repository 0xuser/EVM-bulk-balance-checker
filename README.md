## EVM bulk balance checker
A simple tool to quickly check account balances (including token balances) on various evm-compatible networks. 

### This is demonstration of EVM bulk balance checker
<img src="resources/demo.gif" width="70%" height="70%" alt="Interface Demo">
output:
<img src="resources/output.png" width="70%" height="70%" alt="Output CSV">

### Setup
1. Use `pip install -r requirements.txt` to install all required modules.
2. Use `python main.py` to run.

### Usage
1. Define networks RPCs and tokens in the `config.py` file. 
2. Paste addresses you want to check into `accounts.txt` file, each address should be on a new line.
3. Run `main.py` and select desired network


#### To add custom networks
On the example of BASE network in order to check the balances of Eth and USDC.
1. Add another network to the NETWORKS dictionary in the `config.py` file in the following format:
    ```
       "Base": {
        "rpc": "<your https base rpc>",
        "tokens": {
            "ETH": None,
            "USDC": '0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913'
        }
   ```
2. That's all! you can run the program.


I recommend using private RPCs.
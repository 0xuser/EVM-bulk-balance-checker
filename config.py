SETTINGS = {
    "accounts_file": "accounts.txt",
    "sleep_time": {
        "min": 1,
        "max": 2
    },
    "round": 6,
    "usd_round": 3
}
NETWORKS = {
    "Ethereum": {
        "rpc": "https://eth.llamarpc.com",
        "tokens": {
                "ETH": None,
                "USDC": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                "USDT": "0xdAC17F958D2ee523a2206206994597C13D831ec7"
        }
    },
    "Arbitrum": {
        "rpc": "https://arbitrum.llamarpc.com",
        "tokens": {
            "ETH": None,
            "ARB": "0x912ce59144191c1204e64559fe8253a0e49e6548",
            "USDC": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
            "USDCe": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
            "USDT": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"
        }
    },
    "Optimism": {
        "rpc": "https://optimism.llamarpc.com",
        "tokens": {
            "ETH": None,
            "OP": "0x4200000000000000000000000000000000000042",
            "USDC": "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
            "USDC.e": "0x7F5c764cBc14f9669B88837ca1490cCa17c31607",
            "USDT": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58"
        }
    },
    "Zksync Era": {
        "rpc": "https://mainnet.era.zksync.io",
        "tokens": {
                "ETH": None,
                "USDC": '0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4',
                "nETH": '0x1BbD33384869b30A323e15868Ce46013C82B86FB',
                "rfETH": '0xC5db68F30D21cBe0C9Eac7BE5eA83468d69297e6'
        }
    }
}

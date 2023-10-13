from http import HTTPStatus

import requests


def fetch_price_from_coin_gecko(cryptocurrency_id: str = 'ethereum', vs_currency: str = 'usd', precision: str = '0'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={cryptocurrency_id}&vs_currencies={vs_currency}&precision={precision}'
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        return int(response.json()[cryptocurrency_id][vs_currency])
    else:
        raise Exception(f'Error, can\'t fetch {cryptocurrency_id} price from CoinGecko')
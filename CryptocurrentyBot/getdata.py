import requests
from loguru import logger
from requests import Response


def get_data(coin: str, api_name_coin: str):
    response: Response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={api_name_coin}&vs_currencies=usd')

    if response.status_code == 200:
        data = response.json()

        logger.info(f"Get {coin} " + response.text)
        price = data[f'{api_name_coin}']['usd']

        return f'{coin}: ${price}'
    else:
        logger.error("Превышена скорость запросов!")
        return "Превышена скорость запросов!"


# Tests
if __name__ == '__main__':
    print(get_data("Bitcoin", "bitcoin"))
    print(get_data("BNB", "binancecoin"))
    print(get_data("USDC", "usd-coin"))

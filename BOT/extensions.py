import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoCripto:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise APIException(f"Невозможно конвертировать одинаковые валюты {quote}")

        try:
            platz1 = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")
        try:
            platz2 = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}")
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}")
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={platz1}&tsyms={platz2}")
        nummer2_2 = json.loads(r.content)[keys[quote]]  # {'USD': 221373.29}
        return nummer2_2

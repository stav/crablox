import requests
from fasthtml.common import H1

from config import CMC_API_KEY

id = "CMC_BTC"
path = "/btc"
title = "BTC Market Price"

URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
PARAMS = {"symbol": "BTC", "convert": "USD"}
HEADERS = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": CMC_API_KEY,
}


def get_btc_price():
    response = requests.get(URL, headers=HEADERS, params=PARAMS)
    data = response.json()
    try:
        return data["data"]["BTC"]["quote"]["USD"]["price"]
    except Exception as e:
        print("ERROR::", e, data)
        return 0


def content():
    btc_price = get_btc_price()
    return H1(
        f"BTC Market Price: ${btc_price:.2f}",
        id=id,
    )

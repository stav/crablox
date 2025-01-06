import requests
from fasthtml.common import H1

id = "CMC_BTC"
path = "/btc"
title = "BTC Market Price"

URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
API_KEY = "136881d4-5d87-4fdc-9664-dd81ed465113"
PARAMS = {"symbol": "BTC", "convert": "USD"}
HEADERS = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
}


def get_btc_price():
    response = requests.get(URL, headers=HEADERS, params=PARAMS)
    data = response.json()
    return data["data"]["BTC"]["quote"]["USD"]["price"]


def content():
    btc_price = get_btc_price()
    return H1(
        f"BTC Market Price: ${btc_price:.2f}",
        id=id,
    )

import datetime
import logging

import requests
from fasthtml.common import H1, H2, Div

from config import CMC_API_KEY

logger = logging.getLogger(__name__)

title = "BTC Market Price"
style = "background-color: var(--pico-color-pumpkin-500); border-color: var(--pico-color-pumpkin-300);"

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
        logger.error("Error processing data: %s", e, exc_info=True)
        return 0


def content():
    btc_price = get_btc_price()
    return Div(
        H1("BTC Market Price"),
        H2("Coin Market Cap"),
        H1(f"${btc_price:.2f}", id=id),
        Div(
            f"Server: {datetime.datetime.now()}",
            cls="text-sm",
        ),
    )

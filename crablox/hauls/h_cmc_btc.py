import configparser
import requests
import os
from fasthtml.common import H1

id = "CMC_BTC"
path = "/btc"
title = "BTC Market Price"

# Read config file for api key
file_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(file_path)
mixed_path = os.path.join(parent_dir, "..", "..", "config.ini")
config_file_path = os.path.abspath(mixed_path)
config = configparser.ConfigParser()
config.read(config_file_path)
API_KEY = config["CMC"]["API_KEY"]

URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
PARAMS = {"symbol": "BTC", "convert": "USD"}
HEADERS = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
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

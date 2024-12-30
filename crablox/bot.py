import requests
from bs4 import BeautifulSoup


def get_css_sel(url: str, sel: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.select_one(sel)
    return element

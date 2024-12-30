import csv
from io import StringIO

import requests
from bs4 import BeautifulSoup


def get_css_sel(url: str, sel: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.select_one(sel)
    return element


def get_text(url: str):
    response = requests.get(url)
    return response.text


def _get_rows(url: str):
    response = requests.get(url)
    return csv.reader(StringIO(response.text))


def get_rows_format_1(url: str):
    for row in _get_rows(url):
        try:
            month, year, _, _, index, *_ = row
            yield (
                month,
                year,
                f"{float(index):,.1f}",
            )

        except ValueError:
            print("Invalid data:", row)


def get_rows_format_2(url: str):
    for row in _get_rows(url):
        try:
            month, year, _, current, _, expected, *_ = row
            yield (
                month,
                year,
                f"{float(current):,.1f}",
                f"{float(expected):,.1f}",
            )

        except ValueError:
            print("Invalid data:", row)

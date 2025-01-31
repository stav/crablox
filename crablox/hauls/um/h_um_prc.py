from bot import get_rows_format_2
from .render import render
from . import wrap

id = "UmPrices"
url = "http://www.sca.isr.umich.edu/files/tbcpx1px5.csv"
path = "/um/prices"
title = "UM Prices"


def content():
    details, chart = render(
        url,
        ("Next Year", "Next 5 Years"),
        "Expected Change in Prices",
        get_rows_format_2,
    )
    return chart

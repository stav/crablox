from blocks import block
from bot import get_rows_format_2
from .render import render
from . import wrap

id = "um-prices"
url = "http://www.sca.isr.umich.edu/files/tbcpx1px5.csv"


def prices_block(rt):

    path = "/um/prices"

    @rt(path)
    def get():
        return Prices()

    return block(path, id, "UM Prices")


def Prices():
    return wrap(
        id,
        *render(
            url,
            ("Next Year", "Next 5 Years"),
            "Expected Change in Prices",
            get_rows_format_2,
        )
    )

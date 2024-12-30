from blocks import block
from bot import get_rows_format_1
from .render import render
from . import wrap

url = "http://www.sca.isr.umich.edu/files/tbcics.csv"


def index_block(rt):

    path = "/um/index"

    @rt(path)
    def get():
        return Index()

    return block(path, "index", "UM Index")


def Index():
    return wrap(
        "um-index",
        *render(
            url,
            ("Index",),
            "The Index of Consumer Sentiment",
            get_rows_format_1,
        )
    )

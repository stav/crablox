from blocks import block
from bot import get_rows_format_1
from .render import render
from . import wrap

id = "um-index"
url = "http://www.sca.isr.umich.edu/files/tbcics.csv"


def index_block(rt):

    path = "/um/index"

    @rt(path)
    def get():
        return Index()

    return block(path, id, "UM Index")


def Index():
    return wrap(
        id,
        *render(
            url,
            ("Index",),
            "The Index of Consumer Sentiment",
            get_rows_format_1,
        )
    )

from bot import get_rows_format_1
from .render import render
from . import wrap

id = "UmIndex"
url = "http://www.sca.isr.umich.edu/files/tbcics.csv"
path = "/um/index"
title = "UM Index"


def content():
    return wrap(
        id,
        *render(
            url,
            ("Index",),
            "The Index of Consumer Sentiment",
            get_rows_format_1,
        )
    )

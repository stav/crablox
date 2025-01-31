from bot import get_rows_format_2
from .render import render
from . import wrap

id = "UmComponents"
url = "http://www.sca.isr.umich.edu/files/tbciccice.csv"
path = "/um/components"
title = "UM Components"


def content():
    details, chart = render(
        url,
        ("Current", "Expected"),
        "Components of the Index of Consumer Sentiment",
        get_rows_format_2,
    )
    return chart

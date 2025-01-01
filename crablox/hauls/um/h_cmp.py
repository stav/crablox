from blocks import block
from bot import get_rows_format_2
from .render import render
from . import wrap

id = "um-components"
url = "http://www.sca.isr.umich.edu/files/tbciccice.csv"


def components_block(rt):

    path = "/um/components"

    @rt(path)
    def get():
        return Components()

    return block(path, id, "UM Components")


def Components():
    return wrap(
        id,
        *render(
            url,
            ("Current", "Expected"),
            "Components of the Index of Consumer Sentiment",
            get_rows_format_2,
        )
    )

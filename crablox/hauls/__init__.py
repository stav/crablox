from blocks import block
from bot import get_css_sel, get_text
from .um.h_ics import index_block as um_index_block
from .um.h_prc import prices_block as um_prices_block
from .um.h_cmp import components_block as um_components_block
from .ism.h_mfg import mfg_pmi_block as ism_mfg_block
from .ism.h_srv import srv_pmi_block as ism_srv_block

__all__ = [
    "hello_block",
    "example_block",
    "um_index_block",
    "um_prices_block",
    "um_components_block",
    "tradesties_block",
    "ism_mfg_block",
    "ism_srv_block",
]


def hello_block(rt):

    path = "/hello"

    @rt(path)
    def get():
        return "Hello, World!"

    return block(path, "Hello", "Hello")


def example_block(rt):

    path = "/example"

    @rt(path)
    def get():
        return Example()

    return block(path, "Example", "Example")


def Example():
    return get_css_sel(
        "https://example.com/",
        "body>div",
    )


def tradesties_block(rt):

    path = "/tradesties"

    @rt(path)
    def get():
        return Tradesties()

    return block(path, "Tradesties", "Tradesties")


def Tradesties():
    return get_text(
        "https://tradestie.com/api/v1/apps/reddit",
    )

from blocks import stack
from bot import get_css_sel, get_text

from . import h_bls_esr, h_ism_mfg, h_ism_srv, h_bld_permits, h_cmc_btc, h_gdp
from .um import h_um_ics


blocks = [
    h_ism_mfg,
    h_ism_srv,
    h_um_ics,
    h_bld_permits,
    h_bls_esr,
    h_gdp,
    h_cmc_btc,
]


def hello_block(rt):

    path = "/hello"

    @rt(path)
    def get():
        return "Hello, World!"

    return stack(path, "Hello")


def example_block(rt):

    path = "/example"

    @rt(path)
    def get():
        return Example()

    return stack(path, "Example")


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

    return stack(path, "Tradesties")


def Tradesties():
    return get_text(
        "https://tradestie.com/api/v1/apps/reddit",
    )

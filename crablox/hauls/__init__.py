from blocks import stack
from bot import get_css_sel, get_text

import hauls.h_bld_permits
from .bls import h_esr
from .ism import h_mfg, h_srv
from .um import h_ics, h_prc, h_cmp


blocks = [
    h_mfg,
    h_srv,
    h_ics,
    h_cmp,
    h_prc,
    hauls.h_bld_permits,
    h_esr,
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

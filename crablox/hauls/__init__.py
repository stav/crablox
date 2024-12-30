from blocks import block
from bot import get_css_sel, get_text
from .um.h_ics import index_block as um_index_block


def index_block(rt):

    path = "/index"

    @rt(path)
    def get():
        return "Hello, World!"

    return block(path, "hello", "Hello")


def example_block(rt):

    path = "/example"

    @rt(path)
    def get():
        return Example()

    return block(path, "example", "Example")


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

    return block(path, "tradesties", "Tradesties")


def Tradesties():
    return get_text(
        "https://tradestie.com/api/v1/apps/reddit",
    )

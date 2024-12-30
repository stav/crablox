from blocks import block
from bot import get_css_sel


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

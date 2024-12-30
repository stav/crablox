from fasthtml.common import fast_app, Titled, serve

from style import styles
from blocks import block

app, rt = fast_app(live=True, debug=True, hdrs=[styles])


@rt
def index():
    return (
        Titled(
            "Say Hello to Crablox",
            index_block(rt),
        ),
    )


def index_block(rt):

    path = "/index"

    @rt(path)
    def get():
        return "Hello, World!"

    return block(path, "hello", "Hello")


serve()

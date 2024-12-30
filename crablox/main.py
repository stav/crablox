from fasthtml.common import fast_app, Titled, serve

from style import styles
from plays import index_block, example_block, tradesties_block

app, rt = fast_app(live=True, debug=True, hdrs=[styles])


@rt
def index():
    return (
        Titled(
            "Say Hello to Crablox",
            index_block(rt),
            example_block(rt),
            tradesties_block(rt),
        ),
    )


serve()

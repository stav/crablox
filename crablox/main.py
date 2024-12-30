from fasthtml.common import fast_app, Titled, serve
from fh_altair import altair_headers

from style import styles
from hauls import index_block, example_block, tradesties_block, um_index_block

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])


@rt
def index():
    return (
        Titled(
            "Say Hello to Crablox",
            index_block(rt),
            example_block(rt),
            tradesties_block(rt),
            um_index_block(rt),
        ),
    )


serve()

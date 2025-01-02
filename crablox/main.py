from fasthtml.common import fast_app, Titled, serve
from fh_altair import altair_headers

from style import styles
from hauls import (
    # hello_block,
    # example_block,
    # tradesties_block,
    um_index_block,
    um_prices_block,
    um_components_block,
    ism_mfg_block,
)

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])


@rt
def index():
    return (
        Titled(
            "Say Hello to Crablox",
            # hello_block(rt),
            # example_block(rt),
            # tradesties_block(rt),
            ism_mfg_block(rt),
            um_index_block(rt),
            um_components_block(rt),
            um_prices_block(rt),
        ),
    )


serve()

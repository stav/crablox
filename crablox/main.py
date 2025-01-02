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
    ism_srv_block,
    bld_permits_block,
    bls_esr_block,
)

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])


@app.route("/static/{path:path}")
async def static(request, path):
    return await app.static_file(path, root="./static")


@rt
def index():
    return (
        Titled(
            "Say Hello to Crablox",
            # hello_block(rt),
            # example_block(rt),
            # tradesties_block(rt),
            ism_mfg_block(rt),
            ism_srv_block(rt),
            um_index_block(rt),
            um_components_block(rt),
            um_prices_block(rt),
            bld_permits_block(rt),
            bls_esr_block(rt),
        ),
    )


serve()

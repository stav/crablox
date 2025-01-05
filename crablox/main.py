from types import ModuleType

from fasthtml.common import fast_app, Titled, serve
from fh_altair import altair_headers

import hauls
from blocks import stack
from style import styles

app, rt = fast_app(hdrs=[styles, altair_headers])


@app.route("/static/{path}")
async def static(_request, path: str):
    """
    Serve a static file from the './static' directory.

    Args:
        request: The HTTP request object.
        path (str): The relative path to the static file within the './static' directory.

    Returns:
        The static file response.

    """
    return await app.static_file(path, root="./static")


def create_route(block: ModuleType):
    """
    Creates a route for the given block.

    This function is a wrapper around the `rt` decorator to create a scope for
    the block object at runtime.

    This wrapper creates a route using the block's path. This route is a GET
    request handler that returns the contents of the block.

    Args:
        block: A module object representing a block with: path, id, title, content()

    Returns:
        None
    """

    @rt(block.path)
    def get():
        return block.content()


def block_stacker():
    """
    Generator function that processes hauls and yields a container for each
    block's: path, id, and title.

    Yields:
        The result of the stack function for each block.
    """
    for block in hauls.blocks:
        create_route(block)
        yield stack(block.path, block.id, block.title)


@rt
def index():
    return (
        Titled(
            "Indicator Megaboard Dashboard",
            # hauls.hello_block(rt),
            # hauls.example_block(rt),
            # hauls.tradesties_block(rt),
            *block_stacker(),
        ),
    )


serve()

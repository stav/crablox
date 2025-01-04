from types import ModuleType

from fasthtml.common import fast_app, Titled, serve
from fh_altair import altair_headers

import hauls
from blocks import stack
from style import styles

app, rt = fast_app(live=True, debug=True, hdrs=[styles, altair_headers])


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

    This function takes a block object and creates a route using the block's path.
    It defines a GET request handler that returns the contents of the block. This
    function is a wrapper around the `rt` decorator to create a scope for the block
    object at runtime.

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
    Generator function that processes blocks from hauls and yields stacked blocks.

    For each block in hauls.blocks, this function:
    1. Creates a route for the block using the create_route function.
    2. Yields the result of stacking the block using the stack function with the block's path, id, and title.

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
            "Say Hello to Crablox",
            # hauls.hello_block(rt),
            # hauls.example_block(rt),
            # hauls.tradesties_block(rt),
            *block_stacker(),
        ),
    )


serve()

import os
from types import ModuleType

from fasthtml.common import fast_app, Titled, ScriptX, serve

import hauls
from blocks import stack

env = os.getenv("CRB", "production")
if env == "production":
    from config.prod import fast_config
else:
    from config.dev import fast_config

app, rt = fast_app(**fast_config)
print(f'Using "{env}" environment for {app}')


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
    path = "crablox/main.js"
    return (
        Titled(
            "Indicator Megaboard Dashboard",
            # hauls.hello_block(rt),
            # hauls.example_block(rt),
            # hauls.tradesties_block(rt),
            *block_stacker(),
        ),
        ScriptX(path),
    )


serve()

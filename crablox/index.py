from types import ModuleType

import hauls
from home import page


def route(rt):

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
        def _():
            return block.content()

    # Register block routes
    for block in hauls.blocks:
        print(f"Registering {block.path}")
        create_route(block)

    return page()

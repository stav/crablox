import hauls
import logging
from home import page

# Get a logger for this module
logger = logging.getLogger(__name__)

def route(rt):

    def create_route(block: hauls.Haul):
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

        @rt(f"{block.path}/history")
        def _():
            return block.history()

    # Register block routes
    for block in hauls.blocks:
        create_route(block)

    logger.info(f"Registered {len(hauls.blocks)} blocks")
    return page()

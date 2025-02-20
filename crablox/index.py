from types import ModuleType

from fasthtml.common import (
    A,
    Button,
    Div,
    Img,
    ScriptX,
    Titled,
    Svg,
)
from fa6_icons import svgs

import hauls
from blocks import stack

script_path = "crablox/main.js"


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
        def get():
            print(f"Getting {block.path}")
            return block.content()

    def block_stacker():
        """
        Generator function that processes hauls and yields a container for each
        block's: path, id, and title.

        Yields:
            The result of the stack function for each block.
        """
        for block in hauls.blocks:
            print(f"Registering {block.path}")
            create_route(block)
            yield stack(block.path, block.id, block.title)

    return (
        Titled(
            "Indicator Megaboard Dashboard",
            Div(
                *block_stacker(),
                A(
                    Svg(
                        svgs.arrow_right_from_bracket.solid,
                    ),
                    href="/logout",
                    title="Logout",
                    style="width: 22em; display: flex;",
                ),
                cls="swapy-container",
            ),
        ),
        Div(
            Div(Img(id="lightbox-img"), cls="lightbox-image"),
            Div(id="lightbox-cap", cls="lightbox-caption"),
            Div(id="lightbox-det", cls="lightbox-details"),
            # X closes lightbox, also escape key listener in main.js
            Div(
                Button(
                    "X",
                    cls="crb-close",
                    data_swapy_no_drag=True,
                    title="Try me, or hit escape key",
                ),
                cls="lightbox-close",
                onclick="closeLightbox()",
            ),
            cls="lightbox",
            id="lightbox",
        ),
        ScriptX(script_path),
    )

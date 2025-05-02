from fasthtml.common import (
    A,
    Button,
    Div,
    Img,
    ScriptX,
    Titled,
)
from fasthtml.svg import Svg

from fa6_icons import svgs

import hauls


def page():
    return (
        Titled(
            "Megaboard Indicator Blocks",
            Div(  # Buttons at top of page
                *block_buttons(),
                A(  # Button to open Brandon's dashboard
                    Button("Indicator Dashboard", cls="button secondary"),
                    href="https://docs.google.com/spreadsheets/d/1pla3Y7b7IkSERJRMxXPF-E4IKqpeVOro6k7Pnh8wH4s",
                    target="_blank",
                    title="Brandon's Dashboard",
                    style="margin-left: 0.5em",
                ),
                A(  # Logout button
                    Svg(svgs.arrow_right_from_bracket.solid),
                    href="/logout",
                    title="Logout",
                    cls="button secondary",
                    style="display: inline-flex; margin-left: 1em; vertical-align: middle; width: 2em; height: 2em",
                ),
            ),
            Div(  # Grid for the blocks
                Div(id="block-grid", style="display: none"),
                cls="swapy-container",
            ),
        ),
        Div(  # Lightbox for images
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
            style="background-color: var(--pico-background-color)",
        ),
        # Main client script
        ScriptX("crablox/main.js"),
    )


def block_buttons():
    """
    Generator function that iterates hauls and yields a button for each block.

    We use `hx_on_htmx_after_request` to update Swapy after each button click.

    Add `hx_trigger="revealed,click"` to the button to open all blocks on
    page load, but it causes issues with Swapy, probably because we need to
    debounce the updates.

    Yields:
        A button element for each block.
    """
    for block in hauls.blocks:
        yield Button(
            block.title,
            hx_get=f"/api/blocks/{block.id}",
            hx_target="#block-grid",
            hx_swap="afterend",
            hx_on_htmx_after_request="swapy.update()",
            style=f"margin: 0.2em; {block.style}",
            title=block.summary,
        )

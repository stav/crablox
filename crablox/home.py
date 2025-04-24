from fasthtml.common import (
    A,
    Button,
    Div,
    Img,
    NotStr,
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
                    style="display: inline-flex; vertical-align: middle; margin-left: 1em; width: 2em; height: 2em",
                ),
                cls="button-container",
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

    Needing to update Swapy after each button click is resolved is why we
    use `NotStr` with `on::after-request`; otherwise, we would normally just
    use the `Button` component.

    Yields:
        A button element for each block.
    """
    for block in hauls.blocks:
        yield NotStr(
            # Add hx-trigger revealed to open all blocks on page load
            # but it causes issues with swapy
            f"""
            <button
                hx-get="/api/blocks/{block.id}"
                hx-target="#block-grid"
                hx-swap="afterend"
                hx-on:htmx:after-request="swapy.update()"
                style="margin: 0.2em"
                ignore-hx-trigger="revealed,click"
            >{block.title}</button>"""
        )

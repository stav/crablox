import hashlib
import time

from fasthtml.common import Button, Div, NotStr


def stack(block):

    hash = create_short_hash()
    itemId = f"""{block.id}-{hash}"""

    return (
        Div(  # Slot
            Div(  # Item
                Div(  # Buttons
                    NotStr(  # Open button
                        f"""
                        <button
                            hx-get="{block.path}"
                            hx-target="#{itemId}>.wlv-data"
                            hx-on:htmx:after-request="crbOpenBlock(this)"
                            hx-trigger="revealed,click"
                            class="truncate-text"
                        >{block.title or block.id}</button>"""
                    ),
                    Button(  # Clear button
                        "-",
                        cls="wlv-clear outline",
                        title="Clear",
                        onclick="crbClearBlock(this)",
                    ),
                    Button(  # Close button
                        "X",
                        cls="wlv-close outline",
                        title="Close",
                        onclick="crbCloseBlock(this)",
                    ),
                    Div(  # Handle
                        cls="handle",
                        data_swapy_handle=True,
                    ),
                    cls="crb-buttons",
                ),
                Div(  # Data
                    cls="wlv-data",
                    data_swapy_no_drag=True,
                ),
                cls="item",
                id=itemId,
                data_swapy_item=hash,
            ),
            data_swapy_slot=create_short_hash(),
            cls="wlv-block slot",
        ),
    )


def create_short_hash():
    input_string = str(time.time())
    hash = hashlib.sha256(input_string.encode()).hexdigest()
    return "H" + hash[:8]

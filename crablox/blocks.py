import hashlib
import time

from fasthtml.common import Button, Div


def stack(block):

    hash = create_short_hash()
    itemId = f"""{block.id}-{hash}"""
 
    return (
        Div(  # Slot
            Div(  # Item
                Div(  # Buttons
                    Button(  # Open button
                        block.short,
                        hx_get=block.path,
                        hx_target=f"#{itemId}>.wlv-data",
                        hx_on_htmx_after_request="crbOpenBlock(this)",
                        hx_trigger="revealed,click",
                        style=block.style,
                        cls="truncate-text"
                    ),
                    Button(  # History button
                        "H",
                        title="History",
                        hx_get=f"{block.path}/history",
                        hx_target=f"#{itemId}>.wlv-data",
                        data_history=bool(block.history()),
                        cls="obutton wlv-history outline",
                    ),
                    Button(  # Clear button
                        "-",
                        title="Clear",
                        cls="obutton wlv-clear outline",
                        onclick="crbClearBlock(this)",
                    ),
                    Button(  # Close button
                        "X",
                        title="Close",
                        cls="obutton wlv-close outline",
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

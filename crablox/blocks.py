import hashlib
import time

from fasthtml.common import Button, Div


def stack(path, id, title=None):

    hash = create_short_hash()
    itemId = f"""{id}-{hash}"""

    return (
        Div(  # Slot
            Div(  # Item
                Div(  # Buttons
                    Button(
                        title or id,
                        hx_get=path,
                        hx_target=f"#{itemId}>.wlv-data",
                        onclick="crbOpenBlock(this)",
                    ),
                    Button(
                        "X",
                        cls="wlv-close",
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

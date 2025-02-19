from fasthtml.common import Button, Card, Div


def stack(path, id, title=None):

    client_open_func = f"crbOpenBlock('{id}', '{path}')"

    return (
        Div(  # Slot
            Div(  # Item
                Div(  # Buttons
                    Button(
                        title or id,
                        hx_get=path,
                        hx_target=f"#wlv-{id}-data",
                        onclick=client_open_func,
                        data_swapy_no_drag=True,
                    ),
                    Button(
                        "X",
                        id=f"wlv-{id}-close-button",
                        cls="wlv-close",
                        onclick=f"crbCloseBlock('{id}')",
                        data_swapy_no_drag=True,
                    ),
                    Div(  # Handle
                        cls="handle",
                        data_swapy_handle=True,
                    ),
                    cls="crb-buttons",
                ),
                Div(  # Data
                    id=f"wlv-{id}-data",
                    cls="wlv-data",
                    data_swapy_no_drag=True,
                ),
                data_swapy_item=id,
                cls="item",
            ),
            data_swapy_slot=id,
            cls="wlv-block slot",
        ),
    )

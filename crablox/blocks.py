from fasthtml.common import Button, Card, Div


def stack(path, id, title=None):

    client_open_func = f"crbOpenBlock('{id}', '{path}')"

    return (
        Card(
            Div(id=f"wlv-{id}-data", cls="wlv-data"),
            cls="wlv-block",
            header=Div(
                Button(
                    title or id,
                    # We're not using hx_get because we want a callback to enable the toggle button.
                    # hx_get=path,
                    # hx_target=f"#wlv-{id}-data",
                    onclick=client_open_func,
                ),
                Button(
                    "Details",
                    id=f"wlv-{id}-toggle-button",
                    cls="wlv-toggle",
                    onclick=f"crbToggleDetails('{id}')",
                ),
                Button(
                    "X",
                    id=f"wlv-{id}-close-button",
                    cls="wlv-close",
                    onclick=f"crbCloseBlock('{id}')",
                ),
            ),
        ),
    )

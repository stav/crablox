from fasthtml.common import Button, Card, Div, Script


def stack(path, id, title=None):

    load_script = Script(
        f"""
        document.addEventListener("DOMContentLoaded", function() {{
            const func = 'crbOpenBlock("{id}", "{path}")';
            console.log('Opening 1:', func, crbOpenBlock)
            crbOpenBlock("{id}", "{path}");
            // setTimeout(function() {{
            //     console.log('Opening 2:', func, crbOpenBlock, {id})
            //     crbOpenBlock("{id}", "{path}");
            // }}, 3000);
        }});
        """
    )

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
                    onclick=f"crbOpenBlock('{id}', '{path}')",
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
        # load_script,
    )

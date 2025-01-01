from fasthtml.common import Button, Card, Div, Script


def block(path, id, title):

    script = Script(
        f"""
        function wlv{id}CloseBlock() {{
            document.getElementById('wlv-{id}-data').innerHTML = '';
            document.getElementById('wlv-{id}-close-button').style.display = 'none';
            document.getElementById('wlv-{id}-toggle').style.display = 'none';
        }}
        function wlv{id}OpenBlock() {{
            document.getElementById('wlv-{id}-close-button').style.display = 'inline-block';
            document.getElementById('wlv-{id}-toggle').style.display = 'inline-block';
        }}
        """
    )

    return (
        Card(
            Div(id=f"wlv-{id}-data"),
            cls="wlv-block",
            header=Div(
                Button(
                    title,
                    hx_get=path,
                    hx_target=f"#wlv-{id}-data",
                    hx_trigger="click",
                    onclick=f"wlv{id}OpenBlock()",
                ),
                Button(
                    "X",
                    id=f"wlv-{id}-close-button",
                    cls="wlv-close",
                    onclick=f"wlv{id}CloseBlock()",
                    style="background-color: #c44336; color: white;",
                ),
            ),
        ),
        script,
    )

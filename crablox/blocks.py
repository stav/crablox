from fasthtml.common import Button, Card, Div, Script


def block(path, id, title):

    script = Script(
        f"""
        function wlv{id}CloseBlock() {{
            document.getElementById('wlv-{id}-data').innerHTML = '';
            document.getElementById('wlv-{id}-close-button').style.display = 'none';
            document.getElementById('wlv-{id}-toggle-button').style.display = 'none';
        }}
        function wlv{id}ToggleDetails() {{
            const el = document.querySelector("#{id} article");
            const display = el.style.display;
            el.style.display = (display === 'none' || display === '') ? 'inline-block' : 'none';
        }}
        function wlv{id}OpenBlock() {{
            document.getElementById('wlv-{id}-close-button').style.display = 'inline-block';
            htmx.ajax("GET", "{path}", {{"target": "#wlv-{id}-data"}}).then((e) => {{
                const el = document.querySelector("#{id} article");
                console.log('loaded', e, el);
                if (el) {{
                    document.getElementById('wlv-{id}-toggle-button').style.display = 'inline-block';
                }}
            }});
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
                    # hx_get=path,
                    # hx_target=f"#wlv-{id}-data",
                    onclick=f"wlv{id}OpenBlock()",
                ),
                Button(
                    "Details",
                    id=f"wlv-{id}-toggle-button",
                    cls="wlv-toggle",
                    onclick=f"wlv{id}ToggleDetails()",
                ),
                Button(
                    "X",
                    id=f"wlv-{id}-close-button",
                    cls="wlv-close",
                    onclick=f"wlv{id}CloseBlock()",
                ),
            ),
        ),
        script,
    )

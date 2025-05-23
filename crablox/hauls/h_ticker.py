from fasthtml.common import Card, Div, Form, Input, Button
from ticker import file_name

title = "Lookup"
short = "TL"
style = "background-color: var(--pico-color-purple-800); border-color: var(--pico-color-purple-600);"
caption = "Brandon's Stock Market Cheat Sheet"
summary = caption


def content():
    return Card(
        Form(
            Input(
                type="text",
                name="ticker",
                required=True,
                autofocus=True,
                placeholder="Ticker",
                style="width: 100px; margin-right: 0.5em; display: inline-flex;",
                hx_get="/api/search",
                hx_trigger="keyup changed delay:200ms",
                hx_target="#ticker-suggestions",
            ),
            Button("Lookup", type="submit", cls="button"),
            hx_get="/api/lookup",
            hx_target="closest .wlv-details",
            hx_indicator="#loading-indicator",
            hx_trigger="submit",
            hx_swap="outerHTML",
            hx_on_submit="crbUpdateTicker(this, this.querySelector('input[name=ticker]').value)",
            style="display: inline-flex; margin-left: 0.5em; white-space: nowrap;",
        ),
        Div("Loading...", id="loading-indicator", cls="htmx-indicator"),
        Div(
            id="ticker-suggestions",
            style="position: absolute; z-index: 1000; background: white; border: 1px solid #ccc; max-height: 200px; overflow-y: auto; width: 100px; margin-top: 2px;",
        ),
        Div(id="ticker-result"),
        cls="wlv-details",
        header=(caption, Div(file_name, style="font-family: monospace,monospace;")),
        footer=(),
    )

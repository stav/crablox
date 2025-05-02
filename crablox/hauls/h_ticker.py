from fasthtml.common import Card, Div, Form, Input, Button

title = "Lookup"
short = "TL"
style = "background-color: var(--pico-color-purple-800); border-color: var(--pico-color-purple-600);"
caption = "Ticker Lookup"
summary = "Ticker Lookup"


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
            ),
            Button("Lookup", type="submit", cls="button"),
            hx_get="/api/lookup",
            hx_target="closest .wlv-details",
            style="display: inline-flex; margin-left: 0.5em; white-space: nowrap;",
        ),
        Div(id="ticker-result"),
        cls="wlv-details",
        header="Ticker Lookup",
        footer=(),
    )

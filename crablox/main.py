from fasthtml.common import fast_app, Titled, serve

from style import styles

app, rt = fast_app(live=True, debug=True, hdrs=[styles])


@rt
def index():
    return (
        Titled(
            "Hello, World!",
        ),
    )


serve()

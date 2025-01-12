from fasthtml.common import Div, On


def wrap(id, details, chart):
    toggle = f"""
        const el = document.querySelector("#{id} article");
        console.log(el);
    """

    return Div(
        details,
        Div(
            chart,
            On(code=toggle),
        ),
        id=id,
    )

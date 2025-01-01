from fasthtml.common import Div, On


def wrap(id, card, chart):
    toggle = f"""
        const el = document.querySelector("#{id} article");
        console.log(el);
    """

    return Div(
        card,
        chart,
        On(code=toggle),
        id=id,
    )

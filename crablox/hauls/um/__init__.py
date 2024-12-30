from fasthtml.common import Div, On


def wrap(id, card, chart):
    toggle = f"""
        const el = document.querySelector("#{id} article");
        el.style.display = el.style.display === 'none' ? 'block' : 'none';
    """

    return Div(
        card,
        chart,
        On(code=toggle),
        id=id,
    )

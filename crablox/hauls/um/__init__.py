from fasthtml.common import Div, On


def wrap(id, details, chart, chart2, chart3):
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
        chart2,
        chart3,
        id=id,
    )

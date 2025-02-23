from fasthtml.common import Div, On


def wrap(id, details, chart, chart2, chart3):
    return Div(
        chart,
        chart2,
        chart3,
        details,
        id=id,
    )

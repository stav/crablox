from fasthtml.common import Div


def wrap(id, details, chart, chart2, chart3):
    return Div(
        details,
        chart,
        chart2,
        chart3,
    )

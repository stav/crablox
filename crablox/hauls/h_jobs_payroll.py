from fasthtml.common import Card, Div, Img, P

from .components import get_details, get_history, get_footer

id = "JobsPayroll"
path = "/jobs_payroll"
title = "Empl Situation · 151 K"
short = "ESR"
style = "background-color: var(--pico-color-jade-500); border-color: var(--pico-color-jade-300);"
caption = "US Non-Farm Payrolls"
summary = "Below forecasts, up from a downwardly revised 125K in January"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__)


def content():
    return (
        Div(
            Img(
                src="/static/US_Non_Farm_Payrolls.png",
                alt=caption,
                cls="cbx_image",
                title=summary,
            ),
            onclick="openLightbox(this)",
        ),
        Card(
            Div(details(), cls="marked"),
            cls="wlv-details",
            header=caption,
            footer=get_footer(
                [
                    (
                        "Trading Economics: Non-Farm Payrolls",
                        "https://tradingeconomics.com/united-states/non-farm-payrolls",
                    ),
                    (
                        "BLS: Employment Situation Summary",
                        "https://www.bls.gov/news.release/empsit.nr0.htm",
                    ),
                ],
                history(),
            ),
        ),
    )

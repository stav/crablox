from fasthtml.common import Card, Div, Img, P

from hauls.components import get_details, get_history, get_footer

title = "Sentiment · 52.2"
short = "ICS"
style = "background-color: var(--pico-color-jade-500); border-color: var(--pico-color-jade-300);"
caption = "US Michigan Consumer Sentiment Index"
summary = "Consumer sentiment was unchanged from April, ending four consecutive months of plunging declines."
details_file = "2025-05.md"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__, details_file)


def content():
    return (
        Div(
            Img(
                src="/static/US_Consumer_Confidence.svg",
                alt=caption,
                cls="cbx_image",
                title=summary,
            ),
            onclick="openLightbox(this)",
        ),
        Card(
            Div(details(), cls="marked"),
            P(
                Img(
                    src="/static/um_featured-chart_large-2b6130ca.png",
                    alt="Consumers Express Rising Uncertainty Over Path of Inflation",
                    cls="cbx_image",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/um-index-data.png",
                    alt="UM Index Data",
                    cls="cbx_image",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/um-index-10years.png",
                    alt="UM Index 10 years",
                    cls="cbx_image",
                ),
                onclick="openLightbox(this)",
            ),
            cls="wlv-details",
            header="US Michigan Consumer Sentiment",
            footer=get_footer(
                [
                    (
                        "University of Michigan: Surveys of Consumers",
                        "https://www.sca.isr.umich.edu/",
                    ),
                    (
                        "Trading Economics",
                        "https://tradingeconomics.com/united-states/consumer-confidence",
                    ),
                ],
                history(),
            ),
        ),
    ) 

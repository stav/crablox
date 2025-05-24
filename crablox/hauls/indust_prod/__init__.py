from fasthtml.common import A, Card, Div, Img, Li, Ul, H3, Style

from hauls.components import get_details, get_history

title = "Ind Prod ·  103.88"
short = "Prod"
style = "background-color: var(--pico-color-yellow-500); border-color: var(--pico-color-yellow-300);"
caption = "Industrial Production"
summary = "Industrial Production in the United States decreased 0.4% month-over-month in March 2025, compared to initial estimates of a flat reading."
details_file = "2025-04.md"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__, details_file)


def content():
    return (
        Div(
            Img(
                src="/static/US_Industrial_Production.png",
                alt=caption,
                cls="cbx_image",
                title=summary,
            ),
            onclick="openLightbox(this)",
        ),
        Card(
            Div(details(), cls="marked"),
            cls="wlv-details",
            header="US Industrial Production",
            footer=(
                H3("Resources"),
                Ul(
                    Li(
                        A(
                            "Trading Economics",
                            href="https://tradingeconomics.com/united-states/industrial-production",
                            target="_blank",
                        )
                    ),
                ),
            ),
        ),
        Style(
            """
            ul li {
                margin-bottom: 0.5em;
            }
            """
        ),
    )

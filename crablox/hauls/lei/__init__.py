from fasthtml.common import A, Card, Div, Img, Li, Ul, P, H3, Style

from hauls.components import get_details, get_history

title = "US LEI · 100.5"
short = "LEI"
style = "background-color: var(--pico-color-blue-500); border-color: var(--pico-color-blue-300);"
caption = "US LEI"
summary = "The United States Leading Economic Index increased to 100.50 in March of 2025 over the same month in the previous year."
details_file = "lei.md"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__, details_file)


def content():
    tradingeconomics = "https://tradingeconomics.com/united-states/leading-economic-index"
    conferenceboard = "https://www.conference-board.org/topics/us-leading-indicators"
    skool = "https://www.skool.com/tradingbusiness/money-macro-brief"

    return (
        Div(
            Img(
                src="/static/US_Leading_Economic_Index.svg",
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
                    src="/static/lei-vs-cei.png",
                    cls="cbx_image",
                    alt="US LEI vs CEI indicators over the last 25 years",
                    title="US LEI vs CEI indicators over the last 25 years",
                ),
                onclick="openLightbox(this)",
            ),
            cls="wlv-details",
            header="US LEI",
            footer=(
                H3("Resources"),
                Ul(
                    Li(A("Conference Board", href=conferenceboard, target="_blank")),
                    Li(A("Trading Economics", href=tradingeconomics, target="_blank")),
                    Li(A("Skool", href=skool, target="_blank")),
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

from fasthtml.common import A, Card, Div, Img, Li, Ul, H3, Style

from hauls.components import get_details, get_history

title = "Dur Goods · -0.4%"
short = "Goods"
style = "background-color: var(--pico-color-yellow-500); border-color: var(--pico-color-yellow-300);"
caption = "Durable Goods"
summary = "Durable Goods Orders Excluding Transportation in the United States decreased 0.4% month-over-month in March 2025, compared to initial estimates of a flat reading."
details_file = "2025-03.md"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__, details_file)


def content():
    return (
        Div(
            Img(
                src="/static/US_Durable_Goods_Orders_Ex_Transportation.png",
                alt=caption,
                cls="cbx_image",
                title=summary,
            ),
            onclick="openLightbox(this)",
        ),
        Card(
            Div(details(), cls="marked"),
            cls="wlv-details",
            header="US Durable Goods",
            footer=(
                H3("Resources"),
                Ul(
                    Li(
                        A(
                            "Census Bureau",
                            href="https://www.census.gov/manufacturing/m3/adv/current/index.html",
                            target="_blank",
                        )
                    ),
                    Li(
                        A(
                            "Trading Economics",
                            href="https://tradingeconomics.com/united-states/durable-goods-orders-ex-transportation",
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

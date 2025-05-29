from fasthtml.common import A, Card, Div, Img, Li, Ul, H3, Style

from hauls.components import get_details, get_history

title = "Dur Goods · 0.2%"
short = "Goods"
style = "background-color: var(--pico-color-yellow-500); border-color: var(--pico-color-yellow-300);"
caption = "Durable Goods"
summary = "Durable goods orders excluding transportation in the United States rose by 0.2% month-over-month in April 2025."
details_file = "2025-04.md"
description = """### Description
Durable goods orders excluding transportation, often called "core durable goods orders," measure the change in new orders for long-lasting manufactured goods, excluding transportation equipment. This metric is used to gauge trends in manufacturing activity and economic conditions.
"""


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
            Div(details(), description, cls="marked"),
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
                    Li(
                        A(
                            "Skool",
                            href="https://www.skool.com/tradingbusiness/when-airlines-stop-buying-planes-aprils-durable-goods?p=a394713d",
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

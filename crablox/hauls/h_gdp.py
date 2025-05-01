from fasthtml.common import Card, Div, Img

from .components import get_details, get_history, get_footer

id = "GDP"
path = "/gdp"
title = "GDP · 0.3%"
style = "background-color: var(--pico-color-green-700); border-color: var(--pico-color-green-500);"
caption = "US GDP Growth Rate"
summary = "first negative growth since the first quarter of 22. from 2.4% growth in the previous quarter. 41.3% surge in imports, Consumer spending growth cooled to 1.8%,slowest pace since Q2 23. Federal government expenditures fell 5.1%, steepest drop since Q1 22. In contrast, fixed investment surged 7.8%, the most since Q2 23."


def history():
    return get_history(__file__)


def details():
    return get_details(__file__)


def content():
    return (
        Div(
            Img(
                src="/static/us-gdp-growth-rate.png",
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
                        "BEA: Real gross domestic product (GDP)",
                        "https://www.bea.gov/data/gdp/gross-domestic-product",
                    ),
                    (
                        "Skool: Q4 2024 GDP: The Consumer Camouflage",
                        "https://www.skool.com/tradingbusiness/q4-gdp-the-consumer-camouflage",
                    ),
                ],
                history(),
            ),
        ),
    )

from fasthtml.common import Card, Div, Img, P

from hauls.components import get_details, get_history, get_footer

title = "GDP · -0.5%"
style = "background-color: var(--pico-color-orange-700); border-color: var(--pico-color-orange-500);"
caption = "US GDP Growth Rate"
summary = "The decrease in real GDP in the first quarter primarily reflected an increase in imports..."
details_file = "2025-Q1.md"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__, details_file)


def content():
    return (
        Div(
            Img(
                src="/static/US_GDP_Growth_Rate.svg",
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
                    src="/static/NQ-weekly.png",
                    cls="cbx_image",
                    alt="NQ Weekly",
                    title="NQ Weekly",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/QQQ-weekly.png",
                    cls="cbx_image",
                    alt="QQQ Weekly",
                    title="QQQ Weekly",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/us-gdp.png",
                    cls="cbx_image",
                    alt="US GDP Growth Rate",
                    title="US GDP Growth Rate",
                ),
                onclick="openLightbox(this)",
            ),
            cls="wlv-details",
            header=caption,
            footer=get_footer(
                [
                    (
                        "BEA: Real gross domestic product (GDP)",
                        "https://www.bea.gov/data/gdp/gross-domestic-product",
                    ),
                    (
                        "Skool: Q1 2025 GDP: Final Worse Than Expected",
                        "https://www.skool.com/tradingbusiness/q1-gdp-final-worse-than-expected-yet-new-index-highs",
                    ),
                    (
                        "Trading Economics: United States GDP Growth Rate",
                        "https://tradingeconomics.com/united-states/gdp-growth",
                    ),
                ],
                history(),
            ),
        ),
    ) 

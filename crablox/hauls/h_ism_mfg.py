from fasthtml.common import Card, Div, Img, P

from .components import get_details, get_history, get_footer

title = "ISM Mfg · 49.0"
short = "Mfg"
style = "background-color: var(--pico-color-jade-500); border-color: var(--pico-color-jade-300);"
caption = "ISM Manufacturing PMI"
summary = "We're seeing a significant shift from February's data. The headline PMI has dropped below the growth threshold to 49.0 (down from 50.3), indicating contraction for the first time in recent months."


def history():
    return get_history(__file__)


def details():
    return get_details(__file__)


def content():
    return (
        Div(
            Img(
                src="/static/ism-mfg-pmi.png",
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
                    src="/static/ism-mfg-heatmap.png",
                    cls="cbx_image",
                    alt="ISM Manufacturing Heatmap",
                    title="ISM Manufacturing Heatmap",
                ),
                onclick="openLightbox(this)",
            ),
            cls="wlv-details",
            header=caption,
            footer=get_footer(
                [
                    (
                        "ISM Report on Business",
                        "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/",
                    ),
                    (
                        "Trading Economics: Business Confidence",
                        "https://tradingeconomics.com/united-states/business-confidence#stats",
                    ),
                    (
                        "Manufacturing ISM Update March 2025",
                        "https://www.skool.com/tradingbusiness/manufacturing-ism-update-march-2025?p=281abddc",
                    ),
                ],
                history(),
            ),
        ),
    )

from fasthtml.common import Card, Div, Img, P

from hauls.components import get_details, get_history, get_footer

title = "ISM Srv · 51.6"
short = "Srv"
style = "background-color: var(--pico-color-jade-500); border-color: var(--pico-color-jade-300);"
caption = "ISM Services PMI"
summary = "April Shows Mixed Recovery"
details_file = "2025-04.md"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__, details_file)


def content():
    return (
        Div(
            Img(
                src="/static/ism-srv-pmi.png",
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
                    src="/static/ism-srv-pmi.png",
                    alt=caption,
                    cls="cbx_image",
                    title=summary,
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/ism-srv-bus-act.png",
                    cls="cbx_image",
                    alt="ISM Business Activity",
                    title="ISM Business Activity",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/ism-mfg-prices.png",
                    cls="cbx_image",
                    alt="ISM Manufacturing Prices Paid",
                    title="ISM Manufacturing Prices Paid",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/ism-srv-heatmap.png",
                    cls="cbx_image",
                    alt="ISM Services Heatmap",
                    title="ISM Services Heatmap",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/ism-mfg-srv.png",
                    cls="cbx_image",
                    alt="ISM Manufacturing vs Services",
                    title="ISM Manufacturing vs Services",
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
                        "Trading Economics",
                        "https://tradingeconomics.com/united-states/non-manufacturing-pmi",
                    ),
                    (
                        "Skool",
                        "https://www.skool.com/tradingbusiness/macro-tailrisks?p=df25b53d",
                    ),
                ],
                history(),
            ),
        ),
    ) 

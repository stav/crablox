from fasthtml.common import Card, Div, Img, P

from hauls.components import get_details, get_history, get_footer

title = "ISM Mfg · 48.5"
short = "Mfg"
style = "background-color: var(--pico-color-jade-500); border-color: var(--pico-color-jade-300);"
caption = "ISM Manufacturing PMI"
summary = "🏭 ISM Manufacturing: The month of May Extends Contraction Streak 📉"
details_file = "2025-05.md"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__, details_file)


def content():
    return (
        Div(
            Img(
                src="/static/US_Business_Confidence.svg",
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
            P(
                Img(
                    src="/static/mfg_pmi-vs-gdp.png",
                    cls="cbx_image",
                    alt="ISM Manufacturing PMI vs GDP",
                    title="ISM Manufacturing PMI vs GDP",
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
                        "Skool",
                        "https://www.skool.com/tradingbusiness/ism-manufacturing-may-extends-contraction-streak?p=1d116b3c",
                    ),
                ],
                history(),
            ),
        ),
    ) 

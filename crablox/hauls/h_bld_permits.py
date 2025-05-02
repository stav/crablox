from fasthtml.common import Card, Div, Img, P

from .components import get_details, get_history, get_footer

title = "Bld Permits · 1.47 M"
style = "background-color: var(--pico-color-jade-500); border-color: var(--pico-color-jade-300);"
caption = "United States Building Permits"
summary = "Building permits in the United States rose by 0.5% to a seasonally adjusted annualized rate of 1.467 million in March 2025, compared to the preliminary estimate of a 1.6% increase, final data showed. This marked the first increase after three consecutive months of declines."


def history():
    return get_history(__file__)


def details():
    return get_details(__file__)


def content():
    return (
        Div(
            Img(
                src="/static/US_Building_Permits.svg",
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
                    src="/static/NewResidentialConstruction.png",
                    cls="cbx_image",
                    alt="New Residential Construction for the Last Five Years",
                    title="New Residential Construction for the Last Five Years",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/US_Building_Permits-10years.png",
                    cls="cbx_image",
                    alt="New Residential Construction for the Last Ten Years",
                    title="New Residential Construction for the Last Ten Years",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/NewHousingStarts.gif",
                    cls="cbx_image",
                    alt="New Housing Starts",
                    title="New Housing Starts",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/US_Building_Permits-vs-Housing_starts.png",
                    cls="cbx_image",
                    alt="Building permits Vs Housing starts",
                    title="Building permits Vs Housing starts",
                ),
                onclick="openLightbox(this)",
            ),
            cls="wlv-details",
            header="Building Permits",
            footer=get_footer(
                [
                    (
                        "Census Bureau: New Residential Construction",
                        "https://www.census.gov/construction/nrc/pdf/newresconst.pdf",
                    ),
                    (
                        "Census Bureau: Economic Indicators",
                        "https://www.census.gov/economic-indicators/",
                    ),
                    (
                        "Trading Economics",
                        "https://tradingeconomics.com/united-states/building-permits",
                    ),
                ],
                history(),
            ),
        ),
    )

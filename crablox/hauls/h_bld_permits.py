from fasthtml.common import Card, Div, Img, P

from .components import get_details, get_history, get_footer

id = "BuildingPermits"
path = "/building_permits"
title = "Bld Permits · 1.47 M"
caption = "United States Building Permits"
summary = "Single-family permits went down by 0.2% to an annualized rate of 994 thousand, while permits for buildings with five or more units dropped by 2.5%"


def history():
    return get_history(__file__)


def details():
    return get_details(__file__)


def content():
    return (
        Div(
            Img(
                src="/static/US_Building_Permits.png",
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
                    src="/static/US_Building_Permits-vs-Housing_starts.png",
                    cls="cbx_image",
                    alt="Building permits Vs Housing starts",
                    title="Building permits Vs Housing starts",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/NewResidentialConstruction.png",
                    cls="cbx_image",
                    alt="New Residential Construction for the Last Five Years",
                    title="New Residential Construction for the Last Five Years",
                ),
                onclick="openLightbox(this)",
            ),
            cls="wlv-details",
            header="Building Permits",
            footer=get_footer(
                [
                    (
                        "Census Bureau",
                        "https://www.census.gov/construction/nrc/pdf/newresconst.pdf",
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

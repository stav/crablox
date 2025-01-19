from fasthtml.common import A, Card, Div, H3, H5, Img, Li, P, Ul

id = "BuildingPermits"
path = "/building_permits"
title = "Building Permits"


def content():

    url1 = "https://www.census.gov/construction/nrc/pdf/newresconst.pdf"
    url2 = "https://tradingeconomics.com/united-states/building-permits"

    details = Card(
        H3("United States Building Permits"),
        H5("🏗️ Housing Starts: Analysts Called It Wrong"),
        A(
            Img(
                src="/static/NewResidentialConstruction.png",
                alt="New Residential Construction Chart",
            ),
            href="https://www.census.gov/construction/nrc/pdf/newresconst.pdf",
            target="_blank",
        ),
        cls="wlv-details",
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
            Li(A(url2, href=url2, target="_blank")),
        ),
    )
    return Div(
        details,
        Img(
            src="/static/US_Building_Permits.png",
            alt="United States Building Permits Chart",
        ),
        id=id,
    )

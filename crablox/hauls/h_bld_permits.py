from fasthtml.common import A, Card, Div, H3, H5, Img, Li, P, Ul

id = "BuildingPermits"
path = "/building_permits"
title = "Building Permits"
caption = "United States Building Permits"


def content():

    url1 = "https://www.census.gov/construction/nrc/pdf/newresconst.pdf"
    url2 = "https://tradingeconomics.com/united-states/building-permits"

    details = Card(
        H3("United States Building Permits"),
        P("17 January 2025"),
        H5("🏗️ Housing Starts: Analysts Called It Wrong"),
        P(
            """
            1.499M units, smashing expectations of 1.32M. Biggest print since March 2021.
            The real story is in the details. Multi-family units exploded 58.9% to 418k while single-family barely moved (+3.3%).
            Northeast is absolutely ripping at +40.2% while the West actually cooled off (-0.7%), the Midwest (20% to 204,000), and the South (17.7% to 853,000).
            One the surface, it may look like commercial real estate players are betting big on multi-family. The reality is those guys just want to lock in rates now in fear rates will stay higher for longer or possibly go back up.
            While single-family construction won't budge for the most part until Powell lowers rates more.
            """
        ),
        P(
            Img(
                src="/static/US_Building_Permits-vs-Housing_starts.png",
                cls="cbx_image",
                alt="Building permits Vs Housing starts",
                title="Building permits Vs Housing starts",
            ),
            onclick="openLightbox(this)",
            data_id=id,
        ),
        P(
            Img(
                src="/static/NewResidentialConstruction.png",
                cls="cbx_image",
                alt="New Residential Construction for the Last Five Years",
                title="New Residential Construction for the Last Five Years",
            ),
            onclick="openLightbox(this)",
            data_id=id,
        ),
        cls="wlv-details",
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
            Li(A(url2, href=url2, target="_blank")),
        ),
    )
    return (
        Div(
            Img(
                src="/static/US_Building_Permits.png",
                alt=caption,
                cls="cbx_image",
                title=caption,
            ),
            onclick="openLightbox(this)",
            data_id=id,
        ),
        details,
    )

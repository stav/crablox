from fasthtml.common import A, Card, Div, Img, Li, P, Ul

id = "BuildingPermits"
path = "/building_permits"
title = "Bld Permits · 1.47 M"
caption = "United States Building Permits"
summary = "Single-family permits went down by 0.2% to an annualized rate of 994 thousand, while permits for buildings with five or more units dropped by 2.5%"


def content():

    url1 = "https://www.census.gov/construction/nrc/pdf/newresconst.pdf"
    url2 = "https://tradingeconomics.com/united-states/building-permits"

    details = (
        Div(
            """
# 1.47 M
### United States Building Permits

#### 26 February 2025
Building Permits Final for January 2025 is 1.473 million units.

#### 19 February 2025
Building permits in the United States inched higher by 0.1% to a seasonally adjusted annualized rate of 1.483 million in January of 2025, firmly above market expectations that they would fall to 1.46 million, according to a preliminary estimate. Permits for housing with two to four units surged by 13.2% from the earlier month to 60 thousand, offsetting the 1.4% drop in housing with five or more units (to 427 thousand), while permits for housing with one unit remained unchanged at 996 thousand. Among different regions, permits rose in the West (2.3% to 316 thousand) and the Midwest (1.8% to 223,000). These outweighed the marginal drop in the South (-0.1% to 806 thousand) and the sharper drop in the Northeast (-6.1% to 138 thousand).

_source: U.S. Census Bureau_

#### 17 January 2025

##### 🏗️ Housing Starts: Analysts Called It Wrong

1.499M units, smashing expectations of 1.32M. Biggest print since March 2021.

The real story is in the details. Multi-family units exploded 58.9% to 418k while single-family barely moved (+3.3%).

Northeast is absolutely ripping at +40.2% while the West actually cooled off (-0.7%), the Midwest (20% to 204,000), and the South (17.7% to 853,000).

One the surface, it may look like commercial real estate players are betting big on multi-family. The reality is those guys just want to lock in rates now in fear rates will stay higher for longer or possibly go back up.

While single-family construction won't budge for the most part until Powell lowers rates more.
""",
            cls="marked",
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
        P(
            Img(
                src="/static/NewResidentialConstruction.png",
                cls="cbx_image",
                alt="New Residential Construction for the Last Five Years",
                title="New Residential Construction for the Last Five Years",
            ),
            onclick="openLightbox(this)",
        ),
    )

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
            details,
            cls="wlv-details",
            footer=Ul(
                Li(A(url1, href=url1, target="_blank")),
                Li(A(url2, href=url2, target="_blank")),
            ),
        ),
    )

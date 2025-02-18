from fasthtml.common import A, Card, Div, Img, Li, Ul, H1, H2, H3, H4, P

id = "IsmSrvPmi"
path = "/ism/srv"
title = "ISM Srv 52.8"
caption = "ISM Services PMI "


def content():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/non-manufacturing-pmi"

    details = Card(
        H1("52.8"),
        H2("ISM Services: PMI Growth Slows, but Sector Remains in Expansion"),
        P(
            """
        😮‍💨 Business Activity: 54.5 (-3.5) - biggest yikes of the day
        📉 New Orders: 51.3 (-3.1) - barely keeping its head above water
        🌊 Employment: 52.3 (+1.0) - finally some good news!
        💪 Prices: 60.4 - cooling off (Jerome Powell breathing easier) but still elevated
        """
        ),
        H3("Sector Highlights 🎢"),
        H4("Growth Standouts:"),
        """
            Ag/Forestry/Fishing +14 (from red to leading the pack in growth this month)
            Hotels/Restaurants +13 (people still living their best lives)
            Mining +12 (comeback kid)
            Wholesale Trade +11 (despite the weather fiascos)
        """,
        H4("Industries in Contraction Standouts:"),
        """
            Professional Services: -1 (oof)
            Real Estate: -2 (double oof)
            Other Services: -3 (triple oof)
        """,
        H3("INDUSTRY COMMENTS 💬"),
        industry_comments,
        P(
            Img(
                src="/static/ism-mfg-srv.png",
                cls="cbx_image",
                alt="ISM Manufacturing vs Services",
                title="ISM Manufacturing vs Services",
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
        cls="wlv-details",
        header="ISM Service PMI",
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
            Li(A(url2, href=url2, target="_blank")),
        ),
    )
    return Div(
        details,
        Div(
            Img(
                src="/static/ism-srv-pmi.png",
                alt=caption,
                cls="cbx_image",
                title=caption,
            ),
            onclick="openLightbox(this)",
            data_id=id,
        ),
        id=id,
    )


industry_comments = Div(
    """
#### Wholesale Trade ™
"Business is picking up but still slower than expected for January. We have had a lot of warehouse closures due to weather." 🌨️

#### Healthcare 🏥
"Seeing letters announcing higher pricing from suppliers for 2025. Relying more on analytics to find the lowest impact on cost while keeping the quality high" 💸

#### Educational Services 🏫
"Business conditions seem to be stable for us at this time."

#### Transportation & Warehousing 🚚
“The employment market is softening as we are seeing less natural turn and getting more and better-qualified applicants. Also, requests for our services have continued to increase.”

#### Retail Trade 🏪
“Holiday sales not as robust as hoped for. Will need to adjust future planning.”

#### Information ℹ️
“The paper market is starting to tighten up on the groundwood grades. All the North American mills are pushing dates into late February. It’s not causing any shortages yet, but it’s the first time in over a year that dates are moving out.”

#### Construction 🚧
“Expecting considerable new projects to move to execution by second quarter in the energy market within the U.S.

#### Management of Companies & Support Services 🕴️
“Some apprehension exists with stakeholders and suppliers with government changes and potential tariff burdens.” [Management of Companies & Support Services]

#### Professional, Scientific & Technical Services 🥼
“The threat of tariffs is causing prices to rise. The threat of unstable international markets is resulting in shortages for various materials.”

#### Real Estate, Rental & Leasing 🌇
“Concern going forward is the cost of materials and project work, if any tariffs go into effect.”

### The ISM Divergence 🔄
Manufacturing just hit into growth territory (first time in 2 years!) while services is still hanging on but growing slower. Talk about a divergence.

Trading Take 💡: That cooling price trend might be the move to watch. But that business activity drop? We'll have to keep an eye on that next month as well as this manufacturing/services split.
""",
    cls="marked",
)

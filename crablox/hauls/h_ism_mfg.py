from fasthtml.common import A, Card, Div, Img, Li, Ul, H1, H2

id = "IsmMfgPmi"
path = "/ism/mfg"
title = "ISM Mfg 49.3"


def content():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/business-confidence#stats"

    details = Card(
        H1("49.3"),
        H2("📊 ISM Manufacturing PMI Rises More than Expectation"),
        """
        🔑 Headline: 49.3 (up from 48.4 in November)
        📈 Direction: Still contracting but approaching the expansion threshold of 50
        🚀 Rate of Change: Softest contraction pace since March's expansion

        Key Components:
        📦 New Orders: Strong uptick to 52.5 (highest in 11 months)
        👥 Employment: Declined to 45.3 from 48.1
        Complete Sector Comments 🏭:

        ✅ Growth Sectors:

            Primary Metals: "There is definitely an uptick this month, though not a stable one"

            Electrical Equipment: "The increase in new orders has our plants at full capacity"

            Miscellaneous Manufacturing: "Combo of seasonal factors plus increased demand outlook for 2025"

        ⚠️ Neutral/Mixed:

            Food & Beverage: "We're seeing a softening in sales. This is concerning as it's our peak season"

            Computer & Electronic: "We are constrained by technical labor, despite higher-than-normal backlog"

            Plastics & Rubber: "Orders have increased slightly due to seasonal reasons"

        🔻 Contracting Sectors:

            Transportation Equipment: "Automotive and powersport volume decreases"

            Chemical Products: "Slightly lower due to seasonality and end-of-year destocking"

            Machinery: "Significant slowdown in production requirements in the last two months of the year"

            Fabricated Metal Products: "Order levels well below forecast projections"

        The mix of comments suggests some sectors seeing genuine improvement while others face seasonal and structural challenges.
        """,
        Img(
            src="/static/ism-mfg-glance-2024-nov.png",
            alt="Employment Situation Chart",
        ),
        cls="wlv-details",
        header="ISM Manufacturing PMI",
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
            Li(A(url2, href=url2, target="_blank")),
        ),
    )
    return Div(
        details,
        Img(
            src="/static/ism-mfg-pmi.png",
            alt="Employment Situation Chart",
        ),
        id=id,
    )

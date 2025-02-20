from fasthtml.common import A, Card, Div, Img, Li, Ul, H1, H2, P

id = "IsmMfgPmi"
path = "/ism/mfg"
title = "ISM Mfg 50.9"
caption = "ISM Manufacturing PMI"


def content():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/business-confidence#stats"

    details = Card(
        H1("50.9"),
        H2("📊 Manufacturing sector expands for first time in 26 months!"),
        P("4 February 2025"),
        P("🔑 Headline: 50.9 (up from 49.2 in December)"),
        P("📈 Direction: Expanding"),
        P(
            """
            This marks a significant turning point in manufacturing sector performance,
            with expansion returning after over 2 years of contraction.
            """
        ),
        P(
            """
            Key Highlights:
                ✅ New Orders: 55.1 (+3.0)
                ✅ Production: 52.5 (+2.6)
                ✅ Employment: 50.3 (+4.9)
                ✅ Prices Index: 54.9 (+2.4)
            """
        ),
        P(
            """
            Top Growing Industries (Level):
                1. Textile Mills (+8)
                2. Primary Metals (+7)
                3. Petroleum & Coal Products (+6)
                4. Chemical Products (+5)
                5. Machinery (+4)
            """
        ),
        """
            Notable Industry Comments:
            🧵 Textile Mills: "Looking forward to a year of strong customer demand and higher sales than 2024."
            🏗️ Primary Metals: "Automotive order demand continues to be consistent and on a steady pace. Beginning to look at hiring additional team members once again. Pricing is holding firm."
            ⛽ Chemical Products: "Customer orders slightly stronger than expected. Seeing more general price increases for chemicals/raw materials. No International Longshoremen's strike is a tremendous help."
            🔧 Machinery: "Although we are in our busy season, our demand for the first two weeks of 2025 has outpaced normal levels for this period of time."
            🚗 Transportation Equipment: "Alleviating supply chain conditions are noticeably pivoting back into acute shortage situations. Critical minerals supply chains tightening dramatically due to Chinese restrictions."
            💻 Computer & Electronic Products: "China stimulus is helping us win orders and increase use of services and consumables. Cost pressures remain for all materials and parts but are starting to stabilize."
            🏭 Fabricated Metal Products: "Capital equipment sales are starting off 2025 strong. Normally, we see a soft start to the year, so this strong start is unusual."
            📦 Miscellaneous Manufacturing: "New orders are still good but decreasing compared to previous quarters. Working through current backlog."
            🍔 Food & Beverage: "Volume in 2025 is targeting 2-percent growth. Organization is mindful of potential tariffs and what to do with re-routing or cost increases in supply chains that are impacted."
        """,
        cls="wlv-details",
        header="ISM Manufacturing PMI",
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
            Li(A(url2, href=url2, target="_blank")),
        ),
    )
    return (
        Div(
            Img(
                src="/static/ism-mfg-pmi.png",
                alt=caption,
                cls="cbx_image",
                title=caption,
            ),
            onclick="openLightbox(this)",
            data_id=id,
        ),
        details,
    )

from fasthtml.common import Card, H2, H3, H5, P, Ul, Li, A, Img, Div

id = "GDP"
path = "/gdp"
title = "Gross Domestic Product"


def content():

    url1 = "https://www.skool.com/tradingbusiness/q4-gdp-the-consumer-camouflage"

    details = Card(
        H2("Q4 GDP: 2.3%"),
        H3("🚨 The Consumer Camouflage"),
        H5(
            """2024 Q4 GDP printed today at 2.3%, missing estimates and confirming
           what our ISM charts have been screaming since Q3."""
        ),
        P(
            """
        Consumer spending is masking some serious cracks under the hood.
        Sure, they're spending like it's 2023 (up 4.2%, best since Q1 '23),
        but business investment just went negative for the first time in a year.
        """
        ),
        P(
            """
        There was also massive inventory drawdown shaving almost a full point
        off GDP. Reflecting on what ISM corespondents were saying in Q4,
        businesses were unsure about elections and then had tariff concerns.
        With both fears behind us, this could be setting up for a forced
        inventory rebuild that could give us a head fake later.
        """
        ),
        P(
            """
        Remember how both ISMs took a dive in Q3? They're proving to be the
        canary in the coal mine yet again. We've seen this movie before -
        ISM weakness typically front-runs GDP by 4-6 months, and here we are.
        Now improvement in both ISMs showing Q1 of 2025 could be better than
        last quarter.
        """
        ),
        cls="wlv-details",
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
        ),
    )
    return Div(
        details,
        A(
            Img(
                src="/static/2024-q4-gdp.png",
                alt="US GDP Growth Rate Chart",
                cls="cbx_image",
                onclick="openLightbox(this.src, this.alt)",
            ),
        ),
        id=id,
    )

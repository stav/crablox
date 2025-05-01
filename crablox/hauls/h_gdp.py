from fasthtml.common import Card, H1, H2, H3, H5, P, Ul, Li, A, Img, Div

id = "GDP"
path = "/gdp"
title = "GDP · 2.3%"
style = "background-color: var(--pico-color-green-700); border-color: var(--pico-color-green-500);"
caption = "US GDP Growth Rate"
summary = "Down from 2.8% in Q3. Missing Estimates, business investment just went negative for the first time in a year. Consumer spending  (up 4.2%, best since Q1 '23)"


def content():

    url1 = "https://www.skool.com/tradingbusiness/q4-gdp-the-consumer-camouflage"

    details = Card(
        H1("Q4 2.3%"),
        H2("Gross Domestic Product"),
        H3("🚨 The Consumer Camouflage"),
        P("25 January 2025"),
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
        header=caption,
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
        ),
    )
    return (
        Div(
            Img(
                src="/static/2024-q4-gdp.png",
                alt=caption,
                cls="cbx_image",
                title=summary,
            ),
            onclick="openLightbox(this)",
        ),
        details,
    )

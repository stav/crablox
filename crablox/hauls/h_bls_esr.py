from fasthtml.common import A, Card, Div, Img, Li, Ul

id = "BLS_ESR"
path = "/esr"
title = "Employment Situation Report"


def content():

    url1 = "https://tradingeconomics.com/united-states/non-farm-payrolls"
    url2 = "https://www.bls.gov/news.release/empsit.nr0.htm"

    details = Card(
        """Total nonfarm payroll employment rose by 227,000 in November, and the unemployment rate
        changed little at 4.2 percent, the U.S. Bureau of Labor Statistics reported today. Employment
        trended up in health care, leisure and hospitality, government, and social assistance. Retail
        trade lost jobs.""",
        cls="wlv-details",
        header="Employment Situation Report - November 2024",
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
            Li(A(url2, href=url2, target="_blank")),
        ),
    )
    return Div(
        details,
        Img(
            src="/static/US_Non_Farm_Payrolls.png",
            alt="Employment Situation Chart",
        ),
        id=id,
    )

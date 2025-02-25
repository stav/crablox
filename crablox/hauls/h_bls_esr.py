from fasthtml.common import A, Card, Div, Img, Li, Ul, P, H3

id = "BLS_ESR"
path = "/esr"
title = "Employment Situation Report"
caption = "US Non-Farm Payrolls"


def content():

    url1 = "https://tradingeconomics.com/united-states/non-farm-payrolls"
    url2 = "https://www.bls.gov/news.release/empsit.nr0.htm"

    details = Div(
        """
### Employment Situation Report
United States Non-Farm Payrolls
#### 7 February 2025

Total nonfarm payroll employment rose by 143,000 in January, and the unemployment rate edged down to 4.0 percent, the U.S. Bureau of Labor Statistics reported today. Job gains occurred in health care, retail trade, and social assistance. Employment declined in the mining, quarrying, and oil and gas extraction industry.

#### 10 January 2025
Total nonfarm payroll employment increased by 256,000 in December, and the unemployment rate
    changed little at 4.1 percent, the U.S. Bureau of Labor Statistics reported today. Employment
    trended up in health care, government, and social assistance. Retail trade added jobs in
    December, following a job loss in November.

##### NonFarm Payrolls - Good but Bad
NFP Dec: 256K vs 160K exp (Nov revised to 212K)

- Healthcare +46K
- Retail +43K
- Gov't +33K
- Manufacturing -13K

##### Key points: Huge beat - not even close to estimates.

Nov got revised down but doesn't matter, labor market's still cooking. Retail bounced back hard after that weak Nov.

2024 avg monthly gains = 186K vs 251K in 2023.

Bottom line: Labor market refuses to break. Add in today's hot Michigan inflation expectations and the Fed's got zero reason to cut.

Rates staying higher for even longer.
""",
        cls="marked",
    )
    return (
        Div(
            Img(
                src="/static/US_Non_Farm_Payrolls.png",
                alt=caption,
                cls="cbx_image",
                title=caption,
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

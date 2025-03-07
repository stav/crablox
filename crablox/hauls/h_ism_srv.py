from fasthtml.common import A, Card, Div, Img, Li, Ul, P, Audio

id = "IsmSrvPmi"
path = "/ism/srv"
title = "ISM Srv 53.5"
caption = "ISM Services PMI"
markup = """
# ISM Services PMI
## 53.5
for February 2025
### February Shows Surprising Strength 📈

Hey traders, Just got finished mapping out the February ISM Services data, and unlike manufacturing,
services are showing accelerating growth. The headline PMI rose to 53.5 from 52.8 in January, beating
expectations of 52.6.

Be sure to check out the latest update for the
<a href="https://docs.google.com/spreadsheets/d/1pla3Y7b7IkSERJRMxXPF-E4IKqpeVOro6k7Pnh8wH4s" target="_blank">Indicator Dashboard</a>.

### The Key Numbers

- **Services PMI**        : 53.5 vs 52.8 (+0.7) → Growing faster
- **Business Activity**   : 54.4 vs 54.5 (-0.1) → Growing but slightly slower
- **New Orders**          : 52.2 vs 51.3 (+0.9) → Growing faster
- **Employment**          : 53.9 vs 52.3 (+1.6) → Growing faster
- **Prices**              : 62.6 vs 60.4 (+2.2) → Increasing at a faster pace
- **Supplier Deliveries** : 53.4 vs 53.0 (+0.4) → Slowing at a faster rate
- **Inventories**         : 50.6 vs 47.5 (+3.1) → From contracting to growing
- **Backlog of Orders**   : 51.7 vs 44.8 (+6.9) → From contracting to growing

What's particularly notable here: all four main components (business activity, new orders, employment,
and supplier deliveries) have been expanding for three consecutive months – the first time this has
happened since May 2022.

### Industry Breakdown (Ranked by Performance)

#### Growing Industries (with Level Scores)
- Agriculture, Forestry, Fishing & Hunting (14) 🌾
- Accommodation & Food Services (13) 🍽️
- Mining (12) ⛏️
- Wholesale Trade (11) 🏬
- Finance & Insurance (10) 💰
- Health Care & Social Assistance (9) 🏥
- Educational Services (8) 🎓
- Transportation & Warehousing (7) 🚚
- Retail Trade (6) 🛍️
- Information (5) 💻
- Construction (4) 🏗️
- Management of Companies & Support Services (3)
- Public Administration (2) 🏛️
- Utilities (1) ⚡

#### Neutral Industries (0)
- Arts, Entertainment & Recreation

#### Contracting Industries (Negative Scores)
- Professional, Scientific & Technical Services (-1)
- Real Estate, Rental & Leasing (-2)
- Other Services (-3)

### What They're Saying: Industry Insights

##### 🌾 Agriculture, Forestry, Fishing & Hunting:
"There is great uncertainty about future business activity due to the risk of tariffs and other potential government actions."
##### 🏬 Wholesale Trade:
"Weather has been terrible. When it is not cold and snowy, it seems to be raining. I think that is the biggest hurdle at the moment. The tariff situation has created some uncertainty in the lumber market, but without demand the price of lumber should not move very much. Affordability and high interest rates are still headwinds, but sentiment seems to be good."
##### 🏥 Health Care & Social Assistance:
"The last month has brought multiple weather events. Some locations were closed or delayed opening. Norovirus and other viruses have resulted in busy emergency departments and urgent care facilities."
##### 🚚 Transportation & Warehousing:
"Implementation of tariffs will have a significant cost impact to our projects. The majority of the capital equipment we purchase is not manufactured in the U.S., or components that make the equipment come from overseas manufacturers. We are also seeing U.S. prices already rise in anticipation, which is a similar reaction of the U.S. suppliers when the previous tariffs were introduced."
##### 🍽️ Accommodation & Food Services:
"Tariff actions have created chaos in information and pricing measures, forecasting and forward buys, which may artificially inflate purchases to be followed by a drop off."
##### 🧪 Professional, Scientific & Technical Services (Contracting):
"While our main business remains solid, we are starting to see customers pull out of the sales, with uncertainty again increasing."
##### 📊 Information:
"Tariffs are going to have a ripple down effect that could severely harm our business."
##### 🏛️ Public Administration:
"Observed some continuing uncertainty earlier in the month regarding federal funding levels, but operations have largely normalized as of today."
##### 🎓 Educational Services (Improving):
"The university is still digesting the current potential changes with federal assistance programs."

### Historical Context
Looking at the six-month trend for services:
- Agriculture & Forestry made a dramatic turnaround from -3 in January to +14 in February
- Finance & Insurance jumped from +14 in January to +10 in February
- Educational Services reversed from -2 in January to +8 in February
- Management of Companies moved from -1 in January to +3 in February
- Real Estate flipped from +6 in January to -2 in February

### Trading Implications
The divergence between manufacturing and services is fascinating:
- Services PMI accelerating while manufacturing barely hangs onto expansion
- Both sectors showing significant price pressures (62.6 services vs 62.4 manufacturing)
- Strong employment in services (+1.6) vs contraction in manufacturing (-2.7)
- Services seeing growing backlogs (+6.9) while manufacturing backlogs still contracting

This points to a two-speed economy where domestic service sectors are showing resilience while goods-producing industries face tariff headwinds. The common thread is inflation pressure in both sectors.

For the Fed, this complicates the rate cut picture. With price indices above 62 in both reports and services employment accelerating, the case for near-term cuts is weakening.

Consumer-facing services (accommodation, retail) are showing particular strength, suggesting consumer spending remains healthy despite price pressures.

What macro-sector clues are you getting based on the trends & industry comments? Does this change your inflation outlook?

"""


def content():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/non-manufacturing-pmi"

    return (
        Div(
            Img(
                src="/static/ism-srv-pmi.png",
                alt=caption,
                cls="cbx_image",
                title=caption,
            ),
            onclick="openLightbox(this)",
        ),
        Card(
            Audio(
                controls=True,
                src=f"/audio/{id}",
                type="audio/mpeg",
            ),
            Div(markup, cls="marked"),
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
            header="ISM Services PMI",
            footer=Ul(
                Li(A(url1, href=url1, target="_blank")),
                Li(A(url2, href=url2, target="_blank")),
            ),
        ),
    )

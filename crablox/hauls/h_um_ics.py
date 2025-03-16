from fasthtml.common import A, Card, Div, Img, Li, P, Ul

id = "UmIndex"
url = " http://www.sca.isr.umich.edu/"
path = "/um/index"
title = "Sentiment · 57.9"
caption = "US Michigan Consumer Sentiment"
summary = "Current conditions fell to 53.5 from 65.7, while expectations dropped to 54.2 from 64.0"
markup = """
# 🚨 57.9
## The Index of Consumer Sentiment
#### Sentiment Drags to Multi-Year Lows

### Preliminary Results for March 2025

Just got the latest Michigan numbers and they crashed to 57.9 in March, the lowest we've seen since November 2022. This is way below the 63.1 forecast and marks the third straight monthly decline.

Current conditions fell to 53.5 from 65.7, while expectations dropped to 54.2 from 64.0.

What's particularly concerning is the inflation outlook - year-ahead expectations shot up to 4.9% (highest since late 2022) and the five-year gauge jumped to 3.9%, marking the largest monthly increase since 1993.

The political divide continues to widen dramatically.
<a href="https://data.sca.isr.umich.edu/fetchdoc.php?docid=78161" target="_blank">Looking at our data</a>,
Democratic sentiment has absolutely collapsed to 41.4 in March from 51.3 in February, while Republican sentiment held relatively steady at 83.9. Independents are sliding too, down to 57.2.

This sentiment crash has real trading implications. We're approaching levels typically seen during recessions, and the combination of deteriorating expectations with rising inflation fears screams stagflation. The Fed is in a tough spot with these inflation expectations - rate cuts might be off the table longer than markets expect.

💰 TRADING IMPLICATIONS

This adds another layer of context and creativity for both shorts and longs. If liberal consumers are spending the least, this is another tailrisk for companies who have built a brand around this demographic. Think about which names in retail, consumer discretionary, and even tech for example might be exposed to this demographic spending pullback. The reverse for longs.

### 21 February 2025

📈 The February UMCSI reading just came in and it's ugly. Headline sentiment dropped to 64.7 (from preliminary 67.8), hitting the lowest level since November 2023.

Year-ahead inflation expectations soared to 4.3% (highest since Nov 2023) while five-year outlook jumped to 3.5% from 3.3%. That's the largest monthly increase since May 2021.

Current conditions vs expectations spread widening too. Current conditions gauge fell to 65.7 (from 68.7) while expectations index dropped to 64 (from 67.3). Consumers feel OK now but getting worried about what's ahead.

The 19% collapse in buying intentions for durables really stands out - tariff fears are already hitting consumer behavior before implementation.

There is real risk we might not see the rate cuts markets are expecting this year based on these leading indicators.

#### 💡 Trade Ideas

For longs I'd be careful with consumer discretionary exposure, however this opens up some short ideas in this space.

Hard to see strength there for with purchase intentions falling off a cliff. The 19% collapse in purchasing propensity is too pronounced to dismiss as transitory sentiment. 🛍️

### 7 February 2025

📈 Well, the Fed's "soft landing" narrative just hit some turbulence.

Today's UMich sentiment print is the kind that makes you spill your morning coffee. Headline crashed to 67.8, missing consensus by a country mile. But that's not even the real story here.

The inflation expectations,e're looking at the biggest one-month jump in a decade, shooting up to 4.3%. For context, this type of spike has only happened five times in 14 years.

What's really standing out to me? The long-run inflation expectations. At 3.3%, we're seeing levels not witnessed since 2008. Yes, that 2008. The market's been pricing in rate cuts like they're going out of style, but this report just threw a wrench in that narrative.

The durables data is equally interesting - down 12% on tariff fears. Remember how everyone was calling consumer resilience the backbone of this rally? That backbone's looking a bit wobbly now.

### 10 January 2025

🚨 The first UMCSI reading of 2025 shows some concerning divergences that warrant attention. Headline sentiment dropped to 73.2 (vs. 74.0 prior and 73.8 expected)

The big story isn't the headline miss - it's inflation expectations ripping higher.

Both near-term and long-run jumped to 3.3% (from 2.8%/3.0%).

That's a huge 1-month move we've only seen twice in 4 years.

Current conditions vs expectations spread widening too. Consumers feel OK now but getting worried about what's ahead.

Fed won't like this print on top of the Prices segment of Services ISM going higher too.

There is risk we might not even see another rate cut or two this year now based on these two leading indicators.
"""
details = (
    Div(
        markup,
        cls="marked",
    ),
    P(
        Img(
            src="/static/um_featured-chart_large-2b6130ca.png",
            alt="Consumers Express Rising Uncertainty Over Path of Inflation",
            cls="cbx_image",
        ),
        onclick="openLightbox(this)",
    ),
    P(
        Img(
            src="/static/um-index-data.png",
            alt="UM Index Data",
            cls="cbx_image",
        ),
        onclick="openLightbox(this)",
    ),
)


def content():
    return (
        Div(
            Img(
                src="/static/um-index.png",
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
                Li(A(url, href=url, target="_blank")),
            ),
        ),
    )

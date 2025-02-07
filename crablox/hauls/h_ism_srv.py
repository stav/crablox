from fasthtml.common import A, Card, Div, Img, Li, Ul, H1, H2

id = "IsmSrvPmi"
path = "/ism/srv"
title = "ISM Srv 54.1"


def content():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/non-manufacturing-pmi"

    details = Card(
        H1("54.1"),
        H2("ISM Services: December Beat but Inflation Coming in Hot 🔥"),
        """
        Services PMI crushed expectations - printing 54.1 vs 52.1 last month. The market was looking for 53.3. The service sector is straight up refusing to cool down! This marks the 10th time we're in expansion territory.
        Breaking it down:
        📈 Business Activity: Absolutely ripped higher to 58.2
        🏷️ Prices: Major red flag here - jumped to 64.4 (up 6.2 points). Fed's not gonna like this...
        👥 Employment: Holding steady at 51.4 (tiny -0.1 dip)
        📦 New Orders: Still growing at 54.2
        Rate cut party might get delayed folks. That prices number is no joke - 91 straight months of increases. Powell's probably sweating looking at this report. This may or may not move the needle of FedWatch Futures pricing the next rate cut in June right now, but it can help give us a clue.
        Sector Notes:
        Finance & Insurance leading the pack
        Real Estate getting crushed (no surprise with these higher for longer rates)
        Only 9 sectors growing vs 14 last month - some serious divergence to play with here
        STRONGEST SECTORS:
        🏦 Finance & Insurance: Consistently growing
        🎭 Arts & Entertainment: Solid 13 point jump in Nov, holding strong
        🛍️ Retail: Major comeback story - from contraction to 7 points growth
        WEAKEST LINKS:
        🏠 Real Estate: In the dumps (-6 points) - rates are killing it
        🎓 Education: Dropped hard to -5
        🌾 Agriculture: Whipsawed from +10 to -4 (weird move)
        INTERESTING MOVES:
        🏨 Hotels & Food: Killing it lately (+14 to +3)
        📦 Wholesale: Nice turnaround from -6 in July to +2 now
        💼 Management Services: Can't make up its mind - keeps flip-flopping
        Things I'm Watching:

            Backlogs dropping hard (44.3) - something's not adding up here
            Everyone's freaking about tariffs in the comments (overplayed by some, underplayed by others?)
            Healthcare still can't get their IV supplies straight
            Some offshore moves happening in finance (might be worth digging into)

        Bottom Line: Services sector's still got juice, but there's some complexity in the details. That prices number is the real story here - might shake up the rates timeline everyone's betting on.
        Who's getting macro inspiration from this? Drop your thoughts below 🎯
        """,
        Img(
            src="/static/ism-srv-glance-2024-dec.png",
            alt="Employment Situation Chart",
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
        Img(
            src="/static/ism-srv-pmi.png",
            alt="Employment Situation Chart",
            cls="cbx_image",
            onclick="openLightbox('/static/ism-srv-pmi.png')",
        ),
        id=id,
    )

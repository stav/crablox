from fasthtml.common import A, Card, Div, Img, Li, Ul, Audio

id = "IsmMfgPmi"
path = "/ism/mfg"
title = "ISM Mfg 50.3"
caption = "ISM Manufacturing PMI"
markup = """
# 50.3
## ISM Manufacturing PMI & Macro-Sector Clues 📊
4 March 2025

### 🔑 Headline: 50.3 (down from 50.9 in January)

📈 Direction: Expanding (barely)

The February ISM Manufacturing report just landed, and while the headline PMI
is still in growth territory at 50.3 (down from 50.9), there's a lot happening
beneath the surface that deserves our attention.

### Key Highlights:

- **Index**: 50.3 vs 50.9 (-0.6) → Still growing but slower
- **Orders**: 48.6 vs 55.1 (-6.5) → Flipped from growth to contraction
- **Production**: 50.7 vs 52.5 (-1.8) → Growing but slowing
- **Employment**: 47.6 vs 50.3 (-2.7) → Now contracting
- **Prices**: 62.4 vs 54.9 (+7.5) → Sharply higher
- **Deliveries**: 54.5 vs 50.9 (+3.6) → Slowing, faster rate
- **Inventories**: 49.9 vs 45.9 (+4.0) → Still contracting but improving
- **Backlog**: 46.8 vs 44.9 (+1.9) → Still contracting but improving

The tariff impact is clearly starting to ripple through manufacturing.
That 6.5-point drop in new orders is particularly telling - it's a significant
reversal from January's expansion.

### Industry Breakdown (Ranked by Performance):

#### Growing Industries (with Level Scores)

1. Petroleum & Coal Products (10) 🛢️
1. Miscellaneous Manufacturing (9)
1. Primary Metals (8)
1. Wood Products (7)
1. Food, Beverage & Tobacco Products (6)
1. Electrical Equipment, Appliances & Components (5)
1. Chemical Products (4)
1. Plastics & Rubber Products (3)
1. Fabricated Metal Products (2)
1. Transportation Equipment (1)

#### Neutral Industries (0)

1. Apparel, Leather & Allied Products
1. Printing & Related Support Activities
1. Paper Products

#### Contracting Industries (Negative Scores)

1. Machinery (-1)
1. Computer & Electronic Products (-2)
1. Nonmetallic Mineral Products (-3)
1. Textile Mills (-4)
1. Furniture & Related Products (-5)

#### What They're Saying: Industry Insights

🛢️ **Petroleum & Coal Products**: Leading the pack with the strongest growth score (10).

🏭 **Primary Metals**: "Customer volumes seem to be better than 2024. However, customers are still very hesitant to commit to long-term volumes due to the market uncertainty caused by proposed tariffs on steel/aluminum imports."

🪵 **Wood Products**: Strong performance with a level score of 7.

🍔 **Food & Beverage**: "Inflation and pricing pressure continue to drive uncertainty in our 2025 outlook. We are seeing volume impacts due to pricing, with customers buying less and looking for substitution options."

⚡ **Electrical Equipment**: "New orders continue to be strong after picking up in December. The uncertainty about tariffs keeps us cautious on spending, despite the strong sales right now."

🧪 **Chemical Products**: "The tariff environment regarding products from Mexico and Canada has created uncertainty and volatility among our customers and increased our exposure to retaliatory measures from these countries."

⚙️ **Machinery (Contracting)**: "The incoming tariffs are causing our products to increase in price. Sweeping price increases are incoming from suppliers. Most are noting increases in labor costs. Vendors are indicating open capacity, inflationary concerns are a concern. Our company is working diligently to see how the new tariff will affect our business."

💻 **Computer & Electronic Products (Contracting)**: "Tariff impact has been minimal to overall manufacturing and may remain slight. Limits on U.S. government spending in key organizations like the Food and Drug Administration, Environmental Protection Agency and National Institutes of Health are causing fewer orders."

🧵 **Textile Mills (Contracting)**: Dramatic shift from January's strong performance (+8) to February's contraction (-4).

Meanwhile, Textile Mills experienced the most dramatic reversal, going from +8
in January to -4 in February.

### Trading Implications

What's interesting is the divergence between sectors:

- Energy and domestic commodity plays showing remarkable resilience and even acceleration
- Consumer-facing and tech-related industries struggling with the uncertainty
- Price pressures returning across the board (62.4 price index)

The tariff impact is creating a clear winner/loser dynamic rather than an across-the-board slowdown. Domestic supply chains appear to be benefiting while import-dependent industries are facing headwinds.

With prices surging and new orders contracting, the Fed's rate cut timeline may need reconsideration by the public. Worth watching whether these manufacturing price pressures show up in broader inflation metrics.

What positioning adjustments are you making based on this data? I'm particularly interested in your take.
"""
details = Div(markup, cls="marked")
audio = Audio(
    controls=True,
    src=f"/audio/{id}",
    type="audio/mpeg",
)


def content():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/business-confidence#stats"

    return (
        Div(
            Img(
                src="/static/ism-mfg-pmi.png",
                alt=caption,
                cls="cbx_image",
                title=caption,
            ),
            onclick="openLightbox(this)",
        ),
        Card(
            audio,
            details,
            cls="wlv-details",
            header="ISM Manufacturing PMI",
            footer=Ul(
                Li(A(url1, href=url1, target="_blank")),
                Li(A(url2, href=url2, target="_blank")),
            ),
        ),
    )

from fasthtml.common import A, Card, Div, Img, Li, Ul, P

id = "IsmMfgPmi"
path = "/ism/mfg"
title = "ISM Mfg · 49.0"
caption = "ISM Manufacturing PMI"
summary = "We're seeing a significant shift from February's data. The headline PMI has dropped below the growth threshold to 49.0 (down from 50.3), indicating contraction for the first time in recent months."
with open("crablox/hauls/h_ism_mfg.md", "r") as file:
    markup = file.read()


def content():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/business-confidence#stats"
    url3 = "https://www.skool.com/tradingbusiness/manufacturing-ism-update-march-2025?p=281abddc"

    return (
        Div(
            Img(
                src="/static/ism-mfg-pmi.png",
                alt=caption,
                cls="cbx_image",
                title=summary,
            ),
            onclick="openLightbox(this)",
        ),
        Card(
            Div(markup, cls="marked"),
            P(
                Img(
                    src="/static/ism-mfg-heatmap.png",
                    cls="cbx_image",
                    alt="ISM Manufacturing Heatmap",
                    title="ISM Manufacturing Heatmap",
                ),
                onclick="openLightbox(this)",
            ),
            cls="wlv-details",
            header="ISM Manufacturing PMI",
            footer=Ul(
                Li(A(url1, href=url1, target="_blank")),
                Li(A(url2, href=url2, target="_blank")),
                Li(A(url3, href=url3, target="_blank")),
            ),
        ),
    )

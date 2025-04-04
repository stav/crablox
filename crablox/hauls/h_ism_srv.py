from fasthtml.common import A, Card, Div, Img, Li, Ul, P, Style

id = "IsmSrvPmi"
path = "/ism/srv"
title = "ISM Srv · 50.8"
caption = "ISM Services PMI"
summary = "Macro Tailrisks & Sector Rotation"
with open("crablox/hauls/h_ism_srv.md", "r") as file:
    markup = file.read()


def content():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/non-manufacturing-pmi"
    url3 = "https://www.skool.com/tradingbusiness/macro-tailrisks?p=df25b53d"

    return (
        Div(
            Img(
                src="/static/ism-srv-pmi.png",
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
                Li(A(url3, href=url3, target="_blank")),
            ),
        ),
        Style(
            """
            ul li {
                margin-bottom: 0.5em;
            }
            """
        ),
    )

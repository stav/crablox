from fasthtml.common import A, Card, Div, Img, Li, Ul, P, Style, H3, Button

id = "IsmSrvPmi"
path = "/ism/srv"
title = "ISM Srv · 50.8"
caption = "ISM Services PMI"
summary = "Macro Tailrisks & Sector Rotation"


def details():
    filename = "crablox/hauls/h_ism_srv|.md"
    with open(filename, "r") as file:
        markup = file.read()
        return markup


def content():
    date = "202502"

    skool = "https://www.skool.com/tradingbusiness/macro-tailrisks?p=df25b53d"
    ismworld = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    tradingeconomics = (
        "https://tradingeconomics.com/united-states/non-manufacturing-pmi"
    )

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
            Div(details(), cls="marked"),
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
            footer=(
                H3("History"),
                Ul(
                    Li(
                        Button(
                            date,
                            hx_get=f"/api/ism/srv/history/{date}",
                            hx_target="closest .wlv-data",
                        )
                    ),
                ),
                H3("Resources"),
                Ul(
                    Li(A("ismworld", href=ismworld, target="_blank")),
                    Li(A("tradingeconomics", href=tradingeconomics, target="_blank")),
                    Li(A("skool", href=skool, target="_blank")),
                ),
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

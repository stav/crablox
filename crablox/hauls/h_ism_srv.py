import os

from fasthtml.common import A, Card, Div, Img, Li, Ul, P, Style, H3

title = "ISM Srv · 50.8"
short = "Srv"
style = "background-color: var(--pico-color-jade-500); border-color: var(--pico-color-jade-300);"
caption = "ISM Services PMI"
summary = "Macro Tailrisks & Sector Rotation"
details_filename = "crablox/hauls/h_ism_srv|.md"

current_file = os.path.basename(__file__)
base_name = os.path.splitext(current_file)[0]
directory = os.path.dirname(__file__)
files = os.listdir(directory)


def details():
    """
    Reads and returns the contents of the details markdown file.

    Returns:
        str: The contents of the details markdown file specified by details_filename.
    """
    with open(details_filename, "r") as file:
        return file.read()


def history():
    """
    Generates a list of historical files related to the current module.

    Returns:
        Ul: An unordered list (HTML) containing links to historical files that match
            the current module's base name but are not the current file.
    """

    def matching_files():
        for filename in files:
            if filename.startswith(base_name) and filename != current_file:
                yield filename

    return Ul(
        *[
            Li(
                A(
                    filename,
                    hx_get=f"/api/history/{filename}",
                    hx_target="closest .wlv-data",
                )
            )
            for filename in sorted(matching_files())
        ],
        cls="crb-history-list",
    )


def content():
    """
    Generates the main content for the ISM Services PMI page.

    Returns:
        tuple: A tuple containing:
            - A Div with the main ISM Services PMI image
            - A Card component containing:
                - The details content
                - Multiple images related to ISM Services and Manufacturing
                - A footer with resource links
            - A Style component for list item spacing
    """
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
                    src="/static/ism-srv-pmi.png",
                    alt=caption,
                    cls="cbx_image",
                    title=summary,
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/ism-srv-bus-act.png",
                    cls="cbx_image",
                    alt="ISM Business Activity",
                    title="ISM Business Activity",
                ),
                onclick="openLightbox(this)",
            ),
            P(
                Img(
                    src="/static/ism-mfg-prices.png",
                    cls="cbx_image",
                    alt="ISM Manufacturing Prices Paid",
                    title="ISM Manufacturing Prices Paid",
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
            P(
                Img(
                    src="/static/ism-mfg-srv.png",
                    cls="cbx_image",
                    alt="ISM Manufacturing vs Services",
                    title="ISM Manufacturing vs Services",
                ),
                onclick="openLightbox(this)",
            ),
            cls="wlv-details",
            header="ISM Services PMI",
            footer=(
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

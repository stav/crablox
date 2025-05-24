from fasthtml.common import Card, Div, Img

from hauls.components import get_details, get_history, get_footer

title = "Jobs · 177 K"
short = "Jobs"
style = "background-color: var(--pico-color-yellow-500); border-color: var(--pico-color-yellow-300);"
caption = "US Non-Farm Payrolls"
summary = "🧾 US Adds More Jobs: Complicates Fed's Path 🏦"
details_file = "2025-04.md"


def history():
    return get_history(__file__)


def details():
    details = get_details(__file__, details_file)
    notes = """
### Notes
The United State Bureau of Labor Statistics economic news release called _The Employment Situation_
report is the most widely cited source for U.S. employment data and is released on the first 
Friday of each month and also known as the "Jobs Report" or the "Non-farm Payrolls Report".
        """
    return (details, notes)


def content():
    return (
        Div(
            Img(
                src="/static/US_Non_Farm_Payrolls.png",
                alt=caption,
                cls="cbx_image",
                title=summary,
            ),
            onclick="openLightbox(this)",
        ),
        Card(
            Div(details(), cls="marked"),
            cls="wlv-details",
            header=caption,
            footer=get_footer(
                [
                    (
                        "Trading Economics: Non-Farm Payrolls",
                        "https://tradingeconomics.com/united-states/non-farm-payrolls",
                    ),
                    (
                        "BLS: Employment Situation Summary",
                        "https://www.bls.gov/news.release/empsit.nr0.htm",
                    ),
                ],
                history(),
            ),
        ),
    ) 

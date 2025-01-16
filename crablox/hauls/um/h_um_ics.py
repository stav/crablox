from fasthtml.common import Div, H3, H5, Img, P

from bot import get_rows_format_1
from .render import render
from . import wrap

id = "UmIndex"
url = "http://www.sca.isr.umich.edu/files/tbcics.csv"
path = "/um/index"
title = "UM Index"
details = Div(
    H3("The Index of Consumer Sentiment"),
    H5("Consumer Sentiment Dropped: Inflation Alert 🚨"),
    P(
        """
        The first UMCSI reading of 2025 shows some concerning divergences that warrant attention. Headline sentiment dropped to 73.2 (vs. 74.0 prior and 73.8 expected)
        The big story isn't the headline miss - it's inflation expectations ripping higher.
        Both near-term and long-run jumped to 3.3% (from 2.8%/3.0%).
        That's a huge 1-month move we've only seen twice in 4 years.
        Current conditions vs expectations spread widening too. Consumers feel OK now but getting worried about what's ahead.
        Fed won't like this print on top of the Prices segment of Services ISM going higher too.
        There is risk we might not even see another rate cut or two this year now based on these two leading indicators.
    """
    ),
    Img(
        src="/static/um_featured-chart_large-2b6130ca.png",
        alt="Consumers Express Rising Uncertainty Over Path of Inflation",
    ),
)


def content():
    return wrap(
        id,
        *render(
            url,
            ("Index",),
            details,
            get_rows_format_1,
        )
    )

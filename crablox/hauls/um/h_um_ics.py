from fasthtml.common import Div, H3, H5, Img, P, I

from bot import get_rows_format_1
from . import wrap
from .render import render
from .h_um_cmp import content as cmp_content
from .h_um_prc import content as prc_content

id = "UmIndex"
url = "http://www.sca.isr.umich.edu/files/tbcics.csv"
path = "/um/index"
title = "UM Index"
details = Div(
    H3("The Index of Consumer Sentiment"),
    H5("Consumer Sentiment Drops"),
    P(
        I("""Well, the Fed's "soft landing" narrative just hit some turbulence."""),
    ),
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
    P(
        Img(
            src="/static/um_featured-chart_large-2b6130ca.png",
            alt="Consumers Express Rising Uncertainty Over Path of Inflation",
            cls="cbx_image",
            onclick="openLightbox(this.src, this.alt)",
        ),
    ),
    P(
        Img(
            src="/static/um-index.png",
            alt="United States Michigan Consumer Sentiment",
            cls="cbx_image",
            onclick="openLightbox(this.src, this.alt)",
        ),
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
        ),
        cmp_content(),
        prc_content(),
    )

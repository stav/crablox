from starlette.requests import Request
from fasthtml.common import Div, Dl, Dt, Dd, Button

from ..core import get_ticker_data, search_tickers
from ..utils import format_number


def display(request: Request):
    ticker = request.query_params.get("ticker", "").upper()
    data = lookup(ticker)

    if "error" in data:
        return Div(data["error"])

    return (
        Button(
            "View Time Series",
            cls="ticker-suggestion",
            style="background-color: var(--pico-primary); border: 1px solid var(--pico-secondary)",
            hx_get=f"/timeseries?ticker={ticker}",
            hx_target="#lightbox-det",
            hx_on_click="showTimeSeriesLightbox()",
        ),
        Dl(
            Div(Dt(key), Dd(format_number(value)))
            for key, value in data.items()
            if value is not None
        ),
    )


def lookup(ticker: str):
    data = get_ticker_data(ticker)
    if data is None:
        return {"error": f"No data found for ticker: {ticker}"}
    return data


def search(request: Request):
    query = request.query_params.get("ticker", "").upper()
    print(f"Searching for ({query})")
    if not query:
        return Div("", id="ticker-suggestions")

    matches = search_tickers(query)

    if not matches:
        return Div("No matches found", id="ticker-suggestions")

    return Div(
        *[
            Div(
                f"{ticker} - {company_name}",
                cls="ticker-suggestion",
                style="padding: 4px 8px; cursor: pointer;",
                hx_get=f"/api/lookup?ticker={ticker}",
                hx_target="closest .wlv-details",
                hx_swap="outerHTML",
                hx_indicator="#loading-indicator",
                hx_on_click=f"crbUpdateTicker(this, '{ticker}')",
            )
            for ticker, company_name in matches
        ],
        id="ticker-suggestions",
        style="position: absolute; z-index: 1000; background: white; border: 1px solid #ccc; max-height: 200px; overflow-y: auto; margin-top: 2px;",
    )

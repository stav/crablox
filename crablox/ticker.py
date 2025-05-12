from pathlib import Path

from starlette.requests import Request
from fasthtml.common import Div, Dl, Dt, Dd

from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string

A: int = column_index_from_string("A")

excel_path = Path(__file__).parent.parent / "data" / "US Stock Data 4-25-25.xlsx"


def display(request: Request):
    ticker = request.query_params.get("ticker", "").upper()
    data = lookup(ticker)

    if "error" in data:
        return Div(data["error"])

    return Dl(
        Div(Dt(key), Dd(format_if_number(value)))
        for key, value in data.items()
        if value is not None
    )


def lookup(ticker: str):
    # Load the workbook and get the active sheet
    workbook = load_workbook(excel_path)
    sheet = workbook.active
    if sheet is None:
        return {"error": "No data loaded from workbook"}

    # Get the header row
    headers = [cell.value for cell in sheet[1]]

    # Search for the matching ticker
    for r in range(2, sheet.max_row + 1):
        current_ticker = sheet.cell(row=r, column=A).value
        if current_ticker == ticker:
            # Create a dictionary with headers as keys and corresponding cell values
            return {
                header: sheet.cell(row=r, column=c).value
                for c, header in enumerate(headers, start=1)
            }

    return {"error": f"No data found for ticker: {ticker}"}


def format_if_number(value):
    if not isinstance(value, (int, float)):
        return value

    if value == 0:
        return "0"

    abs_value = abs(value)
    if abs_value >= 1e12:
        return f"{value/1e12:.3f}T"
    elif abs_value >= 1e9:
        return f"{value/1e9:.3f}B"
    elif abs_value >= 1e6:
        return f"{value/1e6:.3f}M"
    elif abs_value >= 1e3:
        return f"{value/1e3:.3f}K"
    else:
        return f"{value:.2f}"


def search(request: Request):
    query = request.query_params.get("ticker", "").upper()
    print(f"Searching for ({query})")
    if not query:
        return Div("", id="ticker-suggestions")
        
    # Load the workbook and get the active sheet
    workbook = load_workbook(excel_path)
    sheet = workbook.active
    if sheet is None:
        return Div("No data loaded from workbook", id="ticker-suggestions")

    # Get all tickers that match the query
    matches = []
    for r in range(2, sheet.max_row + 1):
        current_ticker = sheet.cell(row=r, column=A).value
        if isinstance(current_ticker, str) and current_ticker.startswith(query):
            matches.append(current_ticker)
            if len(matches) >= 10:  # Limit to 10 results
                break

    if not matches:
        return Div("No matches found", id="ticker-suggestions")

    return Div(
        *[
            Div(
                ticker,
                cls="ticker-suggestion",
                style="padding: 4px 8px; cursor: pointer;",
                hx_get=f"/api/lookup?ticker={ticker}",
                hx_target="closest .wlv-details",
                hx_swap="outerHTML",
                hx_indicator="#loading-indicator",
                hx_on_click="crbUpdateTicker(this, this.textContent)",
            )
            for ticker in matches
        ],
        id="ticker-suggestions",
        style="position: absolute; z-index: 1000; background: white; border: 1px solid #ccc; max-height: 200px; overflow-y: auto; width: 100px; margin-top: 2px;",
    )

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

    # fmt: off
    return Dl(
        *[
            Div(Dt(key), Dd(str(value)))
            for key, value in data.items()
            if value is not None
        ]
    )
    # fmt: on


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

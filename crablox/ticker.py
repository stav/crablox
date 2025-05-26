from pathlib import Path
import datetime

import pandas as pd
import yfinance as yf
from starlette.requests import Request
from fasthtml.common import Div, Dl, Dt, Dd, Table, Tr, Th, Td, Button, Caption
from openpyxl.utils import column_index_from_string

from utils import format_market_cap, format_net_income_millions, format_if_number

A: int = column_index_from_string("A")

file_name = "US Stock Data 5-19-25.xlsx"
excel_path = Path(__file__).parent.parent / "data" / file_name

# Module-level DataFrame cache
_df_cache = None

def _load_dataframe():
    global _df_cache
    if _df_cache is None:
        _df_cache = pd.read_excel(excel_path)
    return _df_cache

def display(request: Request):
    ticker = request.query_params.get("ticker", "").upper()
    data = lookup(ticker)

    if "error" in data:
        return Div(data["error"])

    return (
        Button(
            "View Time Series",
            cls="ticker-suggestion",
            style = "margin-top: 2em; background-color: var(--pico-color-blue-500); border-color: var(--pico-color-blue-300);",
            hx_get=f"/timeseries?ticker={ticker}",
            hx_target="#lightbox-det",
            hx_on_click="showTimeSeriesLightbox()",
        ),
        Dl(
            Div(Dt(key), Dd(format_if_number(value)))
            for key, value in data.items()
            if value is not None
        )
    )


def lookup(ticker: str):
    # Use the cached DataFrame
    df = _load_dataframe()
    
    # Find the row matching the ticker
    ticker_data = df[df["Ticker"] == ticker]
    
    if ticker_data.empty:
        return {"error": f"No data found for ticker: {ticker}"}
    
    # Convert the first matching row to a dictionary
    return ticker_data.iloc[0].to_dict()


def search(request: Request):
    query = request.query_params.get("ticker", "").upper()
    print(f"Searching for ({query})")
    if not query:
        return Div("", id="ticker-suggestions")
        
    # Use the cached DataFrame
    df = _load_dataframe()
    
    # Get all tickers that match the query
    matches = df[df["Ticker"].str.startswith(query, na=False)]["Ticker"].tolist()[:10]  # Limit to 10 results

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


def time_series_table(ticker: str):
    # Fetch historical data from yfinance
    company_name = ticker  # Default to ticker if we can't get the company name
    try:
        yf_ticker = yf.Ticker(ticker)
        shares_outstanding = yf_ticker.info.get("sharesOutstanding")
        company_name = yf_ticker.info.get("longName", ticker)  # Get company name, fallback to ticker if not found
        hist = yf_ticker.history(period="5y")
        hist.index = pd.to_datetime(hist.index)
        hist["Year"] = hist.index.year
        avg_price_by_year = hist.groupby("Year")["Close"].mean().to_dict() if not hist.empty else {}
        avg_mcap_by_year = {year: (avg_price_by_year[year] * shares_outstanding) if shares_outstanding else None for year in avg_price_by_year}

        # Fetch Net Income from yfinance financials
        fin = yf_ticker.financials
        net_income_by_year = {}
        if not fin.empty and "Net Income" in fin.index:
            for col in fin.columns:
                try:
                    year = int(str(col)[:4])
                    net_income = fin.at["Net Income", col]
                    if net_income not in (None, 0):
                        net_income_by_year[year] = net_income
                except Exception:
                    continue
    except Exception:
        avg_price_by_year = {}
        avg_mcap_by_year = {}
        net_income_by_year = {}

    # Use the cached DataFrame
    df = _load_dataframe()
    ticker_data = df[df["Ticker"] == ticker]
    if ticker_data.empty:
        return Div(f"No data found for ticker: {ticker}")
    row = ticker_data.iloc[0]

    # Define the years and mapping for each metric
    current_year = datetime.datetime.now().year
    year_suffixes_map = {
        current_year-2: ["FY-1"],
        current_year-1: ["FY0", "F0"],
        current_year+0: ["FY1", "F1"],
        current_year+1: ["FY2", "F2"],
        current_year+2: ["FY3", "F3"]
    }
    years = list(year_suffixes_map.keys())

    # Helper to find the right column for a metric and year
    def find_col(metric, year):
        for suffix in year_suffixes_map.get(year, []):
            for col in df.columns:
                if metric in col and suffix in col:
                    return col
        # fallback: try just the metric and year as string
        for col in df.columns:
            if metric in col and str(year) in col:
                return col
        if metric == "Market Cap" and metric in df.columns:
            return "Market Cap"
        if metric == "Price" and metric in df.columns:
            return "Price"
        return None

    # Metrics and their display names, and any formatting needed
    metrics = [
        ("Stock Price $", "Price", lambda v, y: format_if_number(avg_price_by_year.get(y)) if y <= 2025 and avg_price_by_year.get(y) is not None else ""),
        ("Market Cap $B", "Market Cap", lambda v, y: format_market_cap(avg_mcap_by_year.get(y), v) if y <= 2025 and avg_mcap_by_year.get(y) is not None else ""),
        ("EPS", "EPS", lambda v, y: format_if_number(v)),
        ("Earnings Growth %", "EG", lambda v, y: f"{v:.2f}%" if isinstance(v, (int, float)) and v else ""),
        ("Price/Earnings", "PE", lambda v, y: format_if_number(v)),
        ("PEG", "PEG", lambda v, y: format_if_number(v)),
        ("Sales $M", "Revenue", lambda v, y: f"{v/1e6:.2f}" if isinstance(v, (int, float)) and v else ""),
        ("Revenue Growth %", "Revenue Growth", lambda v, y: f"{v:.2f}%" if isinstance(v, (int, float)) and v else ""),
        ("Revenue Multiple", "PS", lambda v, y: format_if_number(v)),
        ("Net Income $M", "Net Income", lambda v, y: format_net_income_millions(net_income_by_year.get(y)) if y <= 2025 else (f"{v/1e6:.2f}" if isinstance(v, (int, float)) and v else "")),
    ]

    # Build table header
    table_rows = [
        Tr(
            Th("Metrics", style="background: #c97c3b; color: white;"),
            *[Th(str(y), style="background: #c97c3b; color: white;") for y in years]
        )
    ]

    # Build table rows
    for display_name, metric_key, fmt in metrics:
        cells = []
        for year in years:
            col = find_col(metric_key, year)
            val = row[col] if col and col in row else None
            # Creamy background for 2026/2027 price & market cap cells
            if display_name in ("Stock Price $", "Market Cap $B") and year > 2025:
                cell_style = "background: #f8ecd9;"
            elif display_name == "Net Income $M":
                cell_style = "background: #fff;" if year <= 2025 else "background: #f8ecd9;"
            else:
                cell_style = "background: #f8ecd9;" if val is None else ""
            cells.append(Td(fmt(val, year), style=cell_style))
        table_rows.append(
            Tr(
                Th(display_name, style="background: #f8ecd9; text-align: left;"),
                *cells
            )
        )

    return Table(
        Caption(f"{company_name} ({ticker})", style="font-weight: bold"),
        *table_rows,
        style="border-collapse: collapse; width: 100%; background: #f8ecd9;",
        cls="time-series-table"
    )

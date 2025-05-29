from datetime import datetime
from typing import Dict, Optional

from fasthtml.common import Div, Table, Tr, Th, Td, Caption

from ..core import get_ticker_data, get_metrics, fetch_yfinance_data


def time_series_table(ticker: str):
    data = get_ticker_data(ticker)
    if data is None:
        return Div(f"No data found for ticker: {ticker}")

    # Define the years and mapping for each metric
    current_year = datetime.now().year
    year_suffixes_map = {
        current_year - 2: ["FY-1"],
        current_year - 1: ["FY0", "F0"],
        current_year + 0: ["FY1", "F1"],
        current_year + 1: ["FY2", "F2"],
        current_year + 2: ["FY3", "F3"],
    }
    years = list(year_suffixes_map.keys())

    # Helper to find the right column for a metric and year
    def find_col(metric, year):
        for suffix in year_suffixes_map.get(year, []):
            for col in data.keys():
                if metric in col and suffix in col:
                    return col
        # fallback: try just the metric and year as string
        for col in data.keys():
            if metric in col and str(year) in col:
                return col
        if metric == "Market Cap" and metric in data:
            return "Market Cap"
        if metric == "Price" and metric in data:
            return "Price"
        return None

    # Get metrics configuration
    metrics = get_metrics(ticker, current_year)

    # Build table header
    table_rows = [
        Tr(
            Th("Metrics", style="background: var(--pico-color-pumpkin-500); color: white"),
            *[Th(str(y), style="background: var(--pico-color-pumpkin-500); color: white") for y in years],
        )
    ]

    # Build table rows
    for display_name, metric_key, fmt in metrics:
        cells = []

        for year in years:
            col = find_col(metric_key, year)
            val = data.get(col) if col else None

            # Set background for future: price, market cap, net income cells
            if display_name in ("Stock Price $", "Market Cap $B") and year > current_year:
                cell_style = "background: var(--pico-color-pumpkin-50)"
            elif display_name == "Net Income $M":
                cell_style = (
                    "background: white" if year < current_year else "background: var(--pico-color-pumpkin-50)"
                )
            else:
                cell_style = "background: var(--pico-color-pumpkin-50)" if val is None else ""

            cells.append(Td(fmt(val, year), style=cell_style))

        table_rows.append(
            Tr(
                Th(display_name, style="background: var(--pico-color-pumpkin-100); text-align: left;"),
                *cells
            )
        )

    return Table(
        Caption(f"{data['Company Name']} ({ticker})", style="font-weight: bold"),
        *table_rows,
        style="border-collapse: collapse; width: 100%; background: white",
        cls="time-series-table",
    )


def time_series_table_yahoo(ticker: str):
    """
    Generate a time series table for a given ticker using Yahoo Finance data.

    Args:
        ticker: The stock ticker symbol

    Returns:
        A FastHTML Table component containing the time series data
    """
    # Get current year
    current_year = datetime.now().year

    # Fetch data from Yahoo Finance
    (
        avg_price_by_year,
        avg_mcap_by_year,
        net_income_by_year,
        revenue_by_year,
        shares_by_year,
        company_name,
    ) = fetch_yfinance_data(ticker)

    if not avg_price_by_year:
        return Div(f"No Yahoo Finance data found for ticker: {ticker}")

    # Get years to display (current year and 4 years back)
    years = list(range(current_year - 3, current_year + 3))

    # Calculate EPS for all years using historical shares outstanding
    eps_by_year: Dict[int, Optional[float]] = {}
    for year in years:
        net_income = net_income_by_year.get(year)
        shares = shares_by_year.get(year)
        if net_income is not None and shares is not None and shares != 0:
            eps_by_year[year] = net_income / shares
        else:
            eps_by_year[year] = None

    # Calculate earnings growth rate
    earnings_growth_by_year: Dict[int, Optional[float]] = {}
    for i, year in enumerate(years[1:], 1):
        prev_year = years[i - 1]
        prev_eps = eps_by_year.get(prev_year)
        curr_eps = eps_by_year.get(year)
        if prev_eps is not None and curr_eps is not None and prev_eps != 0:
            earnings_growth_by_year[year] = (curr_eps - prev_eps) / abs(prev_eps)
        else:
            earnings_growth_by_year[year] = None

    # Calculate PE ratio
    pe_by_year: Dict[int, Optional[float]] = {}
    for year in years:
        price = avg_price_by_year.get(year)
        eps = eps_by_year.get(year)
        if price is not None and eps is not None and eps != 0:
            pe_by_year[year] = price / eps
        else:
            pe_by_year[year] = None

    # Calculate PEG ratio
    peg_by_year: Dict[int, Optional[float]] = {}
    for year in years:
        pe = pe_by_year.get(year)
        growth = earnings_growth_by_year.get(year)
        if pe is not None and growth is not None and growth != 0:
            peg_by_year[year] = pe / (growth * 100)
        else:
            peg_by_year[year] = None

    # Calculate revenue growth rate
    revenue_growth_by_year: Dict[int, Optional[float]] = {}
    for i, year in enumerate(years[1:], 1):
        prev_year = years[i - 1]
        prev_revenue = revenue_by_year.get(prev_year)
        curr_revenue = revenue_by_year.get(year)
        if prev_revenue is not None and curr_revenue is not None and prev_revenue != 0:
            revenue_growth_by_year[year] = (curr_revenue - prev_revenue) / prev_revenue
        else:
            revenue_growth_by_year[year] = None

    # Calculate revenue multiple (Price/Sales)
    revenue_multiple_by_year: Dict[int, Optional[float]] = {}
    for year in years:
        mcap = avg_mcap_by_year.get(year)
        revenue = revenue_by_year.get(year)
        if mcap is not None and revenue is not None and revenue != 0:
            revenue_multiple_by_year[year] = mcap / revenue
        else:
            revenue_multiple_by_year[year] = None

    # Get metrics to display
    metrics = get_metrics(ticker, current_year)

    # Build table header
    table_rows = [
        Tr(
            Th("Metrics", style="background: var(--pico-color-pumpkin-500); color: white"),
            *[Th(str(y), style="background: var(--pico-color-pumpkin-500); color: white") for y in years],
        )
    ]

    # Add rows for each metric
    for display_name, metric_key, formatter in metrics:
        cells = []
        for year in years:
            if metric_key == "Price":
                value = avg_price_by_year.get(year)
            elif metric_key == "Market Cap":
                value = avg_mcap_by_year.get(year)
            elif metric_key == "EPS":
                value = eps_by_year.get(year)
            elif metric_key == "EG":
                value = earnings_growth_by_year.get(year)
            elif metric_key == "PE":
                value = pe_by_year.get(year)
            elif metric_key == "PEG":
                value = peg_by_year.get(year)
            elif metric_key == "Revenue":
                value = revenue_by_year.get(year)
            elif metric_key == "Revenue Growth":
                value = revenue_growth_by_year.get(year)
            elif metric_key == "PS":
                value = revenue_multiple_by_year.get(year)
            elif metric_key == "Net Income":
                value = net_income_by_year.get(year)
            elif metric_key == "Shares":
                value = shares_by_year.get(year)
            else:
                value = None

            # Set background for future years
            if year > current_year:
                cell_style = "background: var(--pico-color-pumpkin-50)"
            else:
                cell_style = "background: var(--pico-color-pumpkin-50)" if value is None else ""

            cells.append(Td(formatter(value, year), style=cell_style))

        table_rows.append(
            Tr(
                Th(display_name, style="background: var(--pico-color-pumpkin-100); text-align: left;"),
                *cells
            )
        )

    return Table(
        Caption(f"{company_name} ({ticker})", style="font-weight: bold"),
        *table_rows,
        style="border-collapse: collapse; width: 100%; background: white",
        cls="time-series-table",
    )

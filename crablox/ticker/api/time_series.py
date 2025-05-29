import datetime

from fasthtml.common import Div, Table, Tr, Th, Td, Caption

from ..core import get_ticker_data, get_metrics, fetch_yfinance_data


def time_series_table(ticker: str):
    data = get_ticker_data(ticker)
    if data is None:
        return Div(f"No data found for ticker: {ticker}")

    # Define the years and mapping for each metric
    current_year = datetime.datetime.now().year
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
    """Generate a time series table using only Yahoo Finance data."""
    # Get Yahoo Finance data
    avg_price_by_year, avg_mcap_by_year, net_income_by_year, revenue_by_year = fetch_yfinance_data(ticker)
    
    if not avg_price_by_year:
        return Div(f"No Yahoo Finance data found for ticker: {ticker}")

    # Get company info from yfinance
    import yfinance as yf
    yf_ticker = yf.Ticker(ticker)
    company_name = yf_ticker.info.get("longName", ticker)
    shares_outstanding = yf_ticker.info.get("sharesOutstanding")

    # Define the years - only show 2 years back and 2 years forward
    current_year = datetime.datetime.now().year
    years = [current_year - 2, current_year - 1, current_year, current_year + 1, current_year + 2]

    # Build table header
    table_rows = [
        Tr(
            Th("Metrics", style="background: var(--pico-color-pumpkin-500); color: white"),
            *[Th(str(y), style="background: var(--pico-color-pumpkin-500); color: white") for y in years],
        )
    ]

    # Calculate EPS for all years
    eps_by_year = {
        year: (net_income_by_year.get(year) / shares_outstanding if net_income_by_year.get(year) and shares_outstanding else None)
        for year in years
    }

    # Calculate earnings growth for all years
    earnings_growth_by_year = {
        year: (
            ((eps_by_year.get(year) - eps_by_year.get(year-1)) / eps_by_year.get(year-1) * 100) # type: ignore
            if eps_by_year.get(year) is not None and eps_by_year.get(year-1) is not None and eps_by_year.get(year-1) != 0
            else None
        )
        for year in years
    }

    # Calculate P/E for all years
    pe_by_year = {
        year: (
            avg_price_by_year.get(year) / eps_by_year.get(year) # type: ignore
            if avg_price_by_year.get(year) is not None and eps_by_year.get(year) is not None and eps_by_year.get(year) != 0
            else None
        )
        for year in years
    }

    # Calculate revenue growth for all years
    revenue_growth_by_year = {
        year: (
            ((revenue_by_year.get(year) - revenue_by_year.get(year-1)) / revenue_by_year.get(year-1) * 100) # type: ignore
            if revenue_by_year.get(year) is not None and revenue_by_year.get(year-1) is not None and revenue_by_year.get(year-1) != 0
            else None
        )
        for year in years
    }

    # Calculate revenue multiple (P/S) for all years
    ps_by_year = {
        year: (
            (avg_price_by_year.get(year) * shares_outstanding) / revenue_by_year.get(year) # type: ignore
            if avg_price_by_year.get(year) is not None and revenue_by_year.get(year) is not None and revenue_by_year.get(year) != 0 and shares_outstanding
            else None
        )
        for year in years
    }

    # Define metrics to display
    metrics = [
        ("Stock Price $", lambda y: avg_price_by_year.get(y)),
        ("Market Cap $B", lambda y: avg_mcap_by_year.get(y)),
        ("EPS $", lambda y: eps_by_year.get(y)),
        ("Earnings Growth %", lambda y: earnings_growth_by_year.get(y)),
        ("Price/Earnings", lambda y: pe_by_year.get(y)),
        ("PEG", lambda y: (
            pe_by_year.get(y) / earnings_growth_by_year.get(y) # type: ignore
            if pe_by_year.get(y) is not None and earnings_growth_by_year.get(y) is not None and earnings_growth_by_year.get(y) != 0
            else None
        )),
        ("Sales $M", lambda y: revenue_by_year.get(y)),
        ("Revenue Growth %", lambda y: revenue_growth_by_year.get(y)),
        ("Revenue Multiple", lambda y: ps_by_year.get(y)),
        ("Net Income $M", lambda y: net_income_by_year.get(y)),
    ]

    # Build table rows
    for display_name, get_value in metrics:
        cells = []
        for year in years:
            val = get_value(year)
            # Set background for future years
            if year > current_year:
                cell_style = "background: var(--pico-color-pumpkin-50)"
            else:
                cell_style = "background: var(--pico-color-pumpkin-50)" if val is None else ""
            
            if display_name == "Stock Price $":
                formatted_val = f"{val:.2f}" if val is not None else ""
            elif display_name == "Market Cap $B":
                formatted_val = f"{val/1e9:.2f}" if val is not None else ""
            elif display_name == "Net Income $M":
                formatted_val = f"{val/1e6:.0f} M" if val is not None else ""
            elif display_name == "EPS $":
                formatted_val = f"{val:.2f}" if val is not None else ""
            elif display_name == "Earnings Growth %":
                formatted_val = f"{val:+.1f}%" if val is not None else ""
            elif display_name == "Price/Earnings":
                formatted_val = f"{val:.1f}" if val is not None else ""
            elif display_name == "PEG":
                formatted_val = f"{val:.2f}" if val is not None else ""
            elif display_name == "Sales $M":
                formatted_val = f"{val/1e6:.0f} M" if val is not None else ""
            elif display_name == "Revenue Growth %":
                formatted_val = f"{val:+.1f}%" if val is not None else ""
            elif display_name == "Revenue Multiple":
                formatted_val = f"{val:.1f}" if val is not None else ""
            else:
                formatted_val = str(val) if val is not None else ""

            cells.append(Td(formatted_val, style=cell_style))

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

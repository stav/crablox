import datetime

from fasthtml.common import Div, Table, Tr, Th, Td, Caption

from ..core import get_ticker_data, get_metrics


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
            Th("Metrics", style="background: #c97c3b; color: white;"),
            *[Th(str(y), style="background: #c97c3b; color: white;") for y in years],
        )
    ]

    # Build table rows
    for display_name, metric_key, fmt in metrics:
        cells = []
        for year in years:
            col = find_col(metric_key, year)
            val = data.get(col) if col else None
            # Set background for future price & market cap cells
            if display_name in ("Stock Price $", "Market Cap $B") and year > current_year:
                cell_style = "background: #f8ecd9;"
            elif display_name == "Net Income $M":
                cell_style = (
                    "background: #fff;" if year <= current_year else "background: #f8ecd9;"
                )
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
        Caption(f"{data['Company Name']} ({ticker})", style="font-weight: bold"),
        *table_rows,
        style="border-collapse: collapse; width: 100%; background: #f8ecd9;",
        cls="time-series-table",
    )

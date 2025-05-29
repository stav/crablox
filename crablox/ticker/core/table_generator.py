from datetime import datetime
from typing import Dict, List, Optional, Callable, Any, Tuple

from fasthtml.common import Div, Table, Tr, Th, Td, Caption


def create_time_series_table(
    ticker: str,
    company_name: str,
    years: List[int],
    metrics: List[Tuple[str, str, Callable]],
    get_metric_value: Callable[[str, int], Optional[float]],
    current_year: Optional[int] = None,
    future_year_style: str = "background: var(--pico-color-pumpkin-50)",
    empty_cell_style: str = "background: var(--pico-color-pumpkin-50)",
) -> Table:
    """
    Create a time series table with the given data.

    Args:
        ticker: The stock ticker symbol
        company_name: The company name to display
        years: List of years to display
        metrics: List of metric tuples (display_name, metric_key, formatter)
        get_metric_value: Function to get metric value for a given metric key and year
        current_year: Current year for styling future values (defaults to current year)
        future_year_style: CSS style for future year cells
        empty_cell_style: CSS style for empty cells

    Returns:
        A FastHTML Table component containing the time series data
    """
    if current_year is None:
        current_year = datetime.now().year

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
            value = get_metric_value(metric_key, year)

            # Set cell style based on year and value
            if year > current_year:
                cell_style = future_year_style
            else:
                cell_style = empty_cell_style if value is None else ""

            cells.append(Td(fmt(value, year), style=cell_style))

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


def get_excel_metric_value(data: Dict[str, Any], metric_key: str, year: int, year_suffixes_map: Dict[int, List[str]]) -> Optional[float]:
    """Helper function to get metric value from Excel data."""
    # Try to find column with fiscal year suffix
    for suffix in year_suffixes_map.get(year, []):
        for col in data.keys():
            if metric_key in col and suffix in col:
                return data.get(col)

    # Try to find column with year as string
    for col in data.keys():
        if metric_key in col and str(year) in col:
            return data.get(col)

    # Special cases for Market Cap and Price
    if metric_key == "Market Cap" and metric_key in data:
        return data.get("Market Cap")
    if metric_key == "Price" and metric_key in data:
        return data.get("Price")

    return None 

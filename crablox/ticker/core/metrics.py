from typing import Callable, List, Tuple, Dict, Optional, Any
from dataclasses import dataclass
from enum import Enum, auto

from ..utils import format_number, format_number_millions


class MetricSource(Enum):
    """Source of metric data."""
    EXCEL = auto()
    YAHOO = auto()


@dataclass
class Metric:
    """Represents a financial metric to be displayed in the time series table."""
    display_name: str  # Human readable name
    key: str  # Internal key used to identify the metric
    formatter: Callable[[Optional[float], int], str]  # Function to format the value
    source: MetricSource  # Data source for this metric
    description: str  # Description of what the metric represents
    calculation: str  # How the metric is calculated


def get_metrics(ticker: str, current_year: int) -> List[Metric]:
    """
    Get the list of metrics to display in the time series table.

    The metrics are organized by data source (Excel vs Yahoo Finance) and include
    descriptions of what each metric represents and how it's calculated.

    Args:
        ticker: The stock ticker symbol
        current_year: Current year for filtering historical data

    Returns:
        List of Metric objects containing display information and formatting functions
    """
    return [
        # Price and Market Cap (available from both sources)
        Metric(
            display_name="Stock Price $",
            key="Price",
            formatter=lambda v, y: format_number(v),
            source=MetricSource.YAHOO,
            description="Current stock price",
            calculation="Average closing price for the year"
        ),
        Metric(
            display_name="Market Cap $B",
            key="Market Cap",
            formatter=lambda v, y: format_number_millions(v),
            source=MetricSource.YAHOO,
            description="Market capitalization",
            calculation="Price * Shares Outstanding"
        ),

        # Earnings metrics (calculated from Yahoo data)
        Metric(
            display_name="EPS",
            key="EPS",
            formatter=lambda v, y: format_number(v),
            source=MetricSource.YAHOO,
            description="Earnings Per Share",
            calculation="Net Income / Shares Outstanding"
        ),
        Metric(
            display_name="Earnings Growth %",
            key="EG",
            formatter=lambda v, y: format_number(v, ".2%"),
            source=MetricSource.YAHOO,
            description="Year-over-year earnings growth rate",
            calculation="(Current EPS - Previous EPS) / |Previous EPS|"
        ),
        Metric(
            display_name="Price/Earnings",
            key="PE",
            formatter=lambda v, y: format_number(v),
            source=MetricSource.YAHOO,
            description="Price-to-Earnings ratio",
            calculation="Price / EPS"
        ),
        Metric(
            display_name="PEG",
            key="PEG",
            formatter=lambda v, y: format_number(v),
            source=MetricSource.YAHOO,
            description="Price/Earnings to Growth ratio",
            calculation="PE / (Earnings Growth * 100)"
        ),

        # Revenue metrics (calculated from Yahoo data)
        Metric(
            display_name="Sales $M",
            key="Revenue",
            formatter=lambda v, y: format_number_millions(v),
            source=MetricSource.YAHOO,
            description="Total revenue/sales",
            calculation="Total revenue for the year"
        ),
        Metric(
            display_name="Revenue Growth %",
            key="Revenue Growth",
            formatter=lambda v, y: format_number(v, ".2%"),
            source=MetricSource.YAHOO,
            description="Year-over-year revenue growth rate",
            calculation="(Current Revenue - Previous Revenue) / Previous Revenue"
        ),
        Metric(
            display_name="Revenue Multiple",
            key="PS",
            formatter=lambda v, y: format_number(v),
            source=MetricSource.YAHOO,
            description="Price-to-Sales ratio",
            calculation="Market Cap / Revenue"
        ),

        # Additional metrics
        Metric(
            display_name="Net Income $M",
            key="Net Income",
            formatter=lambda v, y: format_number_millions(v),
            source=MetricSource.YAHOO,
            description="Net income/profit",
            calculation="Revenue - Expenses (excluding interest and taxes)"
        ),
        Metric(
            display_name="Shares Outstanding M",
            key="Shares",
            formatter=lambda v, y: format_number_millions(v),
            source=MetricSource.YAHOO,
            description="Number of shares issued",
            calculation="Total shares outstanding"
        ),
    ]


def get_metric_value_yahoo(
    metric_key: str,
    year: int,
    data: Dict[str, Dict[int, Optional[float]]]
) -> Optional[float]:
    """
    Get metric value from Yahoo Finance data.

    Args:
        metric_key: The metric key to look up
        year: The year to get the value for
        data: Dictionary containing all calculated metrics by year

    Returns:
        The metric value for the given year, or None if not available
    """
    return data.get(metric_key, {}).get(year)


def get_metric_value_excel(
    data: Dict[str, Any],
    metric_key: str,
    year: int,
    year_suffixes_map: Dict[int, List[str]]
) -> Optional[float]:
    """
    Get metric value from Excel data.

    Args:
        data: The Excel data dictionary
        metric_key: The metric key to look up
        year: The year to get the value for
        year_suffixes_map: Mapping of years to their fiscal year suffixes

    Returns:
        The metric value for the given year, or None if not available
    """
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

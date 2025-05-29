from typing import Callable, List, Tuple

from ..utils import format_number, format_number_millions


def get_metrics(ticker: str, current_year: int) -> List[Tuple[str, str, Callable]]:
    """
    Get the list of metrics to display in the time series table.

    Args:
        ticker: The stock ticker symbol
        current_year: Current year for filtering historical data

    Returns:
        List of metric tuples containing (display_name, metric_key, formatter_function)
    """
    # fmt: off
    return [
        (
            "Stock Price $", "Price",  # Price = Stock Price
            lambda v, y: format_number(v)
        ),
        (
            "Market Cap $B", "Market Cap",  # Market Capitalization = Price * Shares Outstanding
            lambda v, y: format_number_millions(v)
        ),
        (
            "EPS", "EPS",  # Earnings Per Share = Net Income / Shares Outstanding
            lambda v, y: format_number(v)
        ),
        (
            "Earnings Growth %",  # Earnings Growth Rate = (FY1_EPS - FY0_EPS) / FY0_EPS * 100
            "EG",
            lambda v, y: format_number(v, ".2%")
        ),
        (
            "Price/Earnings", "PE",  # Price-to-Earnings = Price / EPS
            lambda v, y: format_number(v)
        ),
        (
            "PEG", "PEG",  # Price-to-Earnings Growth Ratio = PE / EPS
            lambda v, y: format_number(v)
        ),
        (
            "Sales $M", "Revenue",  # Revenue = Sales
            lambda v, y: format_number_millions(v)
        ),
        (
            "Revenue Growth %", "Revenue Growth",  # Revenue Growth Rate = (FY1_Revenue - FY0_Revenue) / FY0_Revenue * 100
            lambda v, y: format_number(v, ".2%")
        ),
        (
            "Revenue Multiple", "PS",  # Price-to-Sales = Price / Sales
            lambda v, y: format_number(v)
        ),
        (
            "Net Income $M", "Net Income",  # Net Income = Revenue - Expenses (not including interest and taxes)
            lambda v, y: format_number_millions(v)
        ),
        (
            "Shares Outstanding M", "Shares",  # Number of shares issued
            lambda v, y: format_number_millions(v)
        ),
    ]
    # fmt: on

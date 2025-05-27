from typing import Callable, List, Tuple

from .yfinance_data import fetch_yfinance_data as yfd

from ..utils import format_market_cap, format_net_income_millions, format_if_number


def get_metrics(ticker: str, current_year: int) -> List[Tuple[str, str, Callable]]:
    """
    Get the list of metrics to display in the time series table.

    Args:
        ticker: The stock ticker symbol
        current_year: Current year for filtering historical data

    Returns:
        List of metric tuples containing (display_name, metric_key, formatter_function)
    """
    avg_price_by_year, avg_mcap_by_year, net_income_by_year = yfd(ticker)

    # fmt: off
    return [
        (
            "Stock Price $",
            "Price",
            lambda v, y: (
                format_if_number(avg_price_by_year.get(y))
                if y <= current_year and avg_price_by_year.get(y) is not None
                else ""
            ),
        ),
        (
            "Market Cap $B",
            "Market Cap",
            lambda v, y: (
                format_market_cap(avg_mcap_by_year.get(y), v)
                if y <= current_year and avg_mcap_by_year.get(y) is not None
                else ""
            ),
        ),
        (
            "EPS", 
            "EPS", 
            lambda v, y: format_if_number(v)
        ),
        (
            "Earnings Growth %",
            "EG",
            lambda v, y: f"{v:.2f}%" if isinstance(v, (int, float)) and v else "",
        ),
        (
            "Price/Earnings", 
            "PE", 
            lambda v, y: format_if_number(v)
        ),
        (
            "PEG", 
            "PEG", 
            lambda v, y: format_if_number(v)
        ),
        (
            "Sales $M",
            "Revenue",
            lambda v, y: f"{v/1e6:.2f}" if isinstance(v, (int, float)) and v else "",
        ),
        (
            "Revenue Growth %",
            "Revenue Growth",
            lambda v, y: f"{v:.2f}%" if isinstance(v, (int, float)) and v else "",
        ),
        (
            "Revenue Multiple", 
            "PS", 
            lambda v, y: format_if_number(v)
        ),
        (
            "Net Income $M",
            "Net Income",
            lambda v, y: (
                format_net_income_millions(net_income_by_year.get(y))
                if y <= current_year
                else (f"{v/1e6:.2f}" if isinstance(v, (int, float)) and v else "")
            ),
        ),
    ]
    # fmt: on

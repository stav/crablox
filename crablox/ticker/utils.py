from typing import Optional, Any


def format_market_cap(mcap_yf: Optional[float], mcap_excel: Optional[float]) -> str:
    """Format market cap value, preferring yfinance data if available."""
    if mcap_yf is not None:
        return f"{mcap_yf/1e9:.2f}"
    return f"{mcap_excel/1e9:.2f}" if mcap_excel else ""


def format_net_income_millions(net_income: Optional[float]) -> str:
    """Format net income in millions."""
    return f"{net_income/1e6:.2f}" if net_income else ""


def format_if_number(value: Any) -> str:
    """Format a value if it's a number, otherwise return as is."""
    if isinstance(value, (int, float)):
        return f"{value:.2f}"
    return str(value) if value is not None else ""

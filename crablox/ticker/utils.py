from typing import Optional, Any


def format_market_cap(mcap_yf: Optional[float], mcap_excel: Optional[float]) -> str:
    """Format market cap value, preferring yfinance data if available."""
    if mcap_yf is not None:
        return f"{mcap_yf/1e9:.2f}"
    return f"{mcap_excel/1e9:.2f}" if mcap_excel else ""


def format_number(value: Any, format: str = ".2f", suffix: str = "") -> str:
    """Format a value if it's a number, otherwise return as is."""
    if isinstance(value, (int, float)):
        return f"{value:{format}}{suffix}"

    return str(value) if value is not None else ""


def format_number_millions(value: Any) -> str:
    """Format a value into millions."""
    if value is None:
        return ""
    return format_number(value / 1e6, ",.0f", " M")

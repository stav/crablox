"""Utility functions for formatting financial data."""


def format_market_cap(mcap: float | None, fallback: float | None) -> str:
    """Format a market cap value in billions of dollars.

    Args:
        mcap: The primary market cap value in dollars. Can be None or 0.
        fallback: A fallback market cap value in dollars to use if mcap is None or 0.

    Returns:
        A string representation of the value in billions, formatted to 2 decimal places.
        Returns an empty string if both mcap and fallback are None, 0, or invalid.
    """
    if mcap not in (None, 0):
        return f"{mcap/1e9:.2f}"
    elif isinstance(fallback, (int, float)) and fallback:
        return f"{fallback/1e9:.2f}"
    else:
        return ""


def format_net_income_millions(val: float | None) -> str:
    """Format a net income value in millions of dollars.

    Args:
        val: The net income value in dollars. Can be None or 0.

    Returns:
        A string representation of the value in millions, formatted to 2 decimal places.
        Returns an empty string if the input is None or 0.
    """
    if val in (None, 0):
        return ""
    return f"{val/1e6:.2f}"


def format_if_number(value: float | int | None | str) -> str:
    """Format a number with appropriate suffix (K, M, B, T) based on its magnitude.

    Args:
        value: The value to format. Can be a number, None, or any other type.

    Returns:
        A string representation of the number with appropriate suffix.
    """
    if value is None:
        return ""

    if value == 0:
        return "0"

    if not isinstance(value, (int, float)):
        return str(value)

    abs_value = abs(value)
    if abs_value >= 1e12:
        return f"{value/1e12:.3f}T"
    elif abs_value >= 1e9:
        return f"{value/1e9:.3f}B"
    elif abs_value >= 1e6:
        return f"{value/1e6:.3f}M"
    elif abs_value >= 1e3:
        return f"{value/1e3:.3f}K"
    else:
        return f"{value:.2f}"

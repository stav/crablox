from datetime import datetime

from fasthtml.common import Div

from ..core import (
    get_ticker_data,
    get_metrics,
    fetch_yfinance_data,
    calculate_eps,
    calculate_earnings_growth,
    calculate_pe_ratio,
    calculate_peg_ratio,
    calculate_revenue_growth,
    calculate_revenue_multiple,
    get_year_suffixes,
    create_time_series_table,
    get_excel_metric_value,
)


def time_series_table(ticker: str):
    data = get_ticker_data(ticker)
    if data is None:
        return Div(f"No data found for ticker: {ticker}")

    # Define the years and mapping for each metric
    current_year = datetime.now().year
    year_suffixes_map = get_year_suffixes(current_year)
    years = list(year_suffixes_map.keys())

    # Get metrics configuration
    metrics = get_metrics(ticker, current_year)

    def get_metric_value(metric_key: str, year: int):
        return get_excel_metric_value(data, metric_key, year, year_suffixes_map)

    return create_time_series_table(
        ticker=ticker,
        company_name=data["Company Name"],
        years=years,
        metrics=metrics,
        get_metric_value=get_metric_value,
        current_year=current_year,
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

    # Calculate all financial metrics using core functions
    eps_by_year = calculate_eps(net_income_by_year, shares_by_year, years)
    earnings_growth_by_year = calculate_earnings_growth(eps_by_year, years)
    pe_by_year = calculate_pe_ratio(avg_price_by_year, eps_by_year, years)
    peg_by_year = calculate_peg_ratio(pe_by_year, earnings_growth_by_year, years)
    revenue_growth_by_year = calculate_revenue_growth(revenue_by_year, years)
    revenue_multiple_by_year = calculate_revenue_multiple(avg_mcap_by_year, revenue_by_year, years)

    # Get metrics to display
    metrics = get_metrics(ticker, current_year)

    def get_metric_value(metric_key: str, year: int):
        if metric_key == "Price":
            return avg_price_by_year.get(year)
        elif metric_key == "Market Cap":
            return avg_mcap_by_year.get(year)
        elif metric_key == "EPS":
            return eps_by_year.get(year)
        elif metric_key == "EG":
            return earnings_growth_by_year.get(year)
        elif metric_key == "PE":
            return pe_by_year.get(year)
        elif metric_key == "PEG":
            return peg_by_year.get(year)
        elif metric_key == "Revenue":
            return revenue_by_year.get(year)
        elif metric_key == "Revenue Growth":
            return revenue_growth_by_year.get(year)
        elif metric_key == "PS":
            return revenue_multiple_by_year.get(year)
        elif metric_key == "Net Income":
            return net_income_by_year.get(year)
        elif metric_key == "Shares":
            return shares_by_year.get(year)
        return None

    return create_time_series_table(
        ticker=ticker,
        company_name=company_name,
        years=years,
        metrics=metrics,
        get_metric_value=get_metric_value,
        current_year=current_year,
    )

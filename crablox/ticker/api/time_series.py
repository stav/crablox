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
    get_metric_value_excel,
    get_metric_value_yahoo,
    get_year_range,
    MetricSource,
)


def time_series_table(ticker: str):
    """
    Generate a hybrid time series table combining data from both Excel and Yahoo Finance.

    This function combines data from both sources according to specific rules:
    - Stock price and market cap: Yahoo (current_year-2 to current_year-1), Excel (current_year), blank (current_year+1 to current_year+2)
    - EPS: Excel for all years
    - Earnings Growth: Yahoo (current_year-2), Excel (current_year-1 to current_year+2)
    - PEG: Yahoo (current_year-2 to current_year-1), Excel (current_year to current_year+2)
    - Sales: Excel for all years
    - Revenue Growth: Yahoo (current_year-2), Excel (current_year-1 to current_year+2)
    - Revenue Multiple: Excel for all years
    - Net Income: Yahoo (current_year-2 to current_year-1), blank (current_year to current_year+2)
    - Shares: Yahoo for all years

    Args:
        ticker: The stock ticker symbol

    Returns:
        A FastHTML Table component containing the hybrid time series data
    """
    # Get Excel data
    excel_data = get_ticker_data(ticker)
    if excel_data is None:
        return Div(f"No Excel data found for ticker: {ticker}")

    # Get current year dynamically
    current_year = datetime.now().year
    year_suffixes_map = get_year_suffixes(current_year)
    years = get_year_range(current_year)

    # Fetch Yahoo Finance data
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

    # Get metrics configuration
    metrics = get_metrics(ticker, current_year)

    def get_metric_value(metric_key: str, year: int):
        # Stock Price and Market Cap
        if metric_key in ("Price", "Market Cap"):
            if year in (current_year - 2, current_year - 1):
                return get_metric_value_yahoo(metric_key, year, {
                    "Price": {k: v for k, v in avg_price_by_year.items()},
                    "Market Cap": {k: v for k, v in avg_mcap_by_year.items()},
                })
            elif year == current_year:
                return get_metric_value_excel(excel_data, metric_key, year, year_suffixes_map)
            return None

        # EPS - Excel for all years
        if metric_key == "EPS":
            return get_metric_value_excel(excel_data, metric_key, year, year_suffixes_map)

        # Earnings Growth - Yahoo for current_year-2, Excel for rest
        if metric_key == "EG":
            if year == current_year - 2:
                eps = calculate_eps(net_income_by_year, shares_by_year, [current_year - 3, current_year - 2])
                eg = calculate_earnings_growth(eps, [current_year - 3, current_year - 2])
                return get_metric_value_yahoo(metric_key, year, {
                    "EG": {k: v for k, v in eg.items()},
                })
            return get_metric_value_excel(excel_data, metric_key, year, year_suffixes_map)

        # PEG - Yahoo for current_year-2 and current_year-1, Excel for rest
        if metric_key == "PEG":
            if year in (current_year - 2, current_year - 1):
                eps = calculate_eps(net_income_by_year, shares_by_year, [current_year - 3, current_year - 2, current_year - 1])
                eg = calculate_earnings_growth(eps, [current_year - 3, current_year - 2, current_year - 1])
                pe = calculate_pe_ratio(avg_price_by_year, eps, [current_year - 3, current_year - 2, current_year - 1])
                peg = calculate_peg_ratio(pe, eg, [current_year - 3, current_year - 2, current_year - 1])
                return get_metric_value_yahoo(metric_key, year, {
                    "PEG": {k: v for k, v in peg.items()},
                })
            return get_metric_value_excel(excel_data, metric_key, year, year_suffixes_map)

        # PE - Yahoo for current_year-2 and current_year-1, Excel for rest
        if metric_key == "PE":
            if year in (current_year - 2, current_year - 1):
                eps = calculate_eps(net_income_by_year, shares_by_year, [current_year - 3, current_year - 2, current_year - 1])
                pe = calculate_pe_ratio(avg_price_by_year, eps, [current_year - 3, current_year - 2, current_year - 1])
                return get_metric_value_yahoo(metric_key, year, {
                    "PE": {k: v for k, v in pe.items()},
                })
            return get_metric_value_excel(excel_data, metric_key, year, year_suffixes_map)

        # Sales - Excel for all years
        if metric_key == "Revenue":
            return get_metric_value_excel(excel_data, metric_key, year, year_suffixes_map)

        # Revenue Growth - Yahoo for current_year-2, Excel for rest
        if metric_key == "Revenue Growth":
            if year == current_year - 2:
                rg = calculate_revenue_growth(revenue_by_year, [current_year - 3, current_year - 2])
                return get_metric_value_yahoo(metric_key, year, {
                    "Revenue Growth": {k: v for k, v in rg.items()},
                })
            return get_metric_value_excel(excel_data, metric_key, year, year_suffixes_map)

        # Revenue Multiple - Excel for all years
        if metric_key == "PS":
            return get_metric_value_excel(excel_data, metric_key, year, year_suffixes_map)

        # Net Income - Yahoo for current_year-2 and current_year-1, blank for rest
        if metric_key == "Net Income":
            if year in (current_year - 2, current_year - 1):
                return get_metric_value_yahoo(metric_key, year, {
                    "Net Income": {k: v for k, v in net_income_by_year.items()},
                })
            return None

        # Shares - Yahoo for all years
        if metric_key == "Shares":
            return get_metric_value_yahoo(metric_key, year, {
                "Shares": {k: v for k, v in shares_by_year.items()},
            })

        return None

    return create_time_series_table(
        ticker=ticker,
        company_name=company_name,
        years=years,
        metrics=metrics,
        get_metric_value=get_metric_value,
        current_year=current_year,
        source=MetricSource.EXCEL,  # Using EXCEL as source for styling rules to keep white backgrounds for cells with data
    )


def time_series_table_excel(ticker: str):
    """
    Generate a time series table for a given ticker using Excel data.

    This function uses data from the Excel spreadsheet to display financial metrics
    over time. The data is organized by fiscal years with suffixes (e.g., FY1, F1).

    Args:
        ticker: The stock ticker symbol

    Returns:
        A FastHTML Table component containing the time series data
    """
    data = get_ticker_data(ticker)
    if data is None:
        return Div(f"No data found for ticker: {ticker}")

    # Define the years and mapping for each metric
    current_year = datetime.now().year
    year_suffixes_map = get_year_suffixes(current_year)
    years = get_year_range(current_year)

    # Get metrics configuration
    metrics = get_metrics(ticker, current_year)

    def get_metric_value(metric_key: str, year: int):
        return get_metric_value_excel(data, metric_key, year, year_suffixes_map)

    return create_time_series_table(
        ticker=ticker,
        company_name=data["Company Name"],
        years=years,
        metrics=metrics,
        get_metric_value=get_metric_value,
        current_year=current_year,
        source=MetricSource.EXCEL,
    )


def time_series_table_yahoo(ticker: str):
    """
    Generate a time series table for a given ticker using Yahoo Finance data.

    This function uses data from Yahoo Finance to display financial metrics over time.
    The data includes historical values and projections. Growth rates and ratios are
    calculated from the raw data.

    Note: To calculate growth rates and ratios for the earliest year, we need data
    from the previous year. For example, to calculate growth rates for current_year-2,
    we need current_year-3 data as a baseline.

    Args:
        ticker: The stock ticker symbol

    Returns:
        A FastHTML Table component containing the time series data
    """
    # Get current year and year range
    current_year = datetime.now().year
    # We need 3 years of data to calculate growth rates and ratios for the earliest year
    years = get_year_range(current_year, lookback_years=3)

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

    # Calculate all financial metrics using core functions
    eps_by_year = calculate_eps(net_income_by_year, shares_by_year, years)
    earnings_growth_by_year = calculate_earnings_growth(eps_by_year, years)
    pe_by_year = calculate_pe_ratio(avg_price_by_year, eps_by_year, years)
    peg_by_year = calculate_peg_ratio(pe_by_year, earnings_growth_by_year, years)
    revenue_growth_by_year = calculate_revenue_growth(revenue_by_year, years)
    revenue_multiple_by_year = calculate_revenue_multiple(avg_mcap_by_year, revenue_by_year, years)

    # Get metrics to display
    metrics = get_metrics(ticker, current_year)

    # Organize all metrics into a single dictionary for easy lookup
    metric_data = {
        "Price": avg_price_by_year,
        "Market Cap": avg_mcap_by_year,
        "EPS": eps_by_year,
        "EG": earnings_growth_by_year,
        "PE": pe_by_year,
        "PEG": peg_by_year,
        "Revenue": revenue_by_year,
        "Revenue Growth": revenue_growth_by_year,
        "PS": revenue_multiple_by_year,
        "Net Income": net_income_by_year,
        "Shares": shares_by_year,
    }

    def get_metric_value(metric_key: str, year: int):
        return get_metric_value_yahoo(metric_key, year, metric_data)

    return create_time_series_table(
        ticker=ticker,
        company_name=company_name,
        years=years[1:],  # Skip the first year because it was ust used to calulate EPS
        metrics=metrics,
        get_metric_value=get_metric_value,
        current_year=current_year,
        source=MetricSource.YAHOO,
    )

from pathlib import Path
import pandas as pd
from openpyxl.utils import column_index_from_string
import logging

logger = logging.getLogger(__name__)

A: int = column_index_from_string("A")
B: int = column_index_from_string("B")

file_name = "US Stock Data 5-19-25.xlsx"
excel_path = Path(__file__).parent.parent.parent.parent / "data" / file_name

# Module-level DataFrame cache
_df_cache = None


def load_dataframe():
    """Load and cache the stock data DataFrame."""
    global _df_cache
    if _df_cache is None:
        logger.info(f"Cache miss: Loading stock data from '{excel_path}'")
        _df_cache = pd.read_excel(excel_path)
    return _df_cache


def get_ticker_data(ticker: str):
    """Get data for a specific ticker."""
    df = load_dataframe()
    ticker_data = df[df["Ticker"] == ticker]
    if ticker_data.empty:
        return None
    data = ticker_data.iloc[0].to_dict()
    # Add company name from column B
    data["Company Name"] = ticker_data.iloc[0, B - 1]  # -1 because pandas is 0-indexed
    return data


def search_tickers(query: str, limit: int = 10):
    """Search for tickers matching the query in either ticker symbol or company name.
    Returns a list of tuples containing (ticker, company_name)."""
    df = load_dataframe()
    # Filter rows where Ticker starts with query or Company Name contains query
    ticker_matches = df["Ticker"].str.startswith(query, na=False)
    company_matches = df.iloc[:, B - 1].str.contains(query, case=False, na=False)  # B-1 is company name column
    filtered_df = df[ticker_matches | company_matches]
    # Get both Ticker and Company Name columns
    result_df = filtered_df[["Ticker", filtered_df.columns[B - 1]]]
    # Convert to list of tuples and limit results
    matches = list(zip(result_df["Ticker"], result_df.iloc[:, 1]))[:limit]
    return matches

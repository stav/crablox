from pathlib import Path
import pandas as pd
from openpyxl.utils import column_index_from_string

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
    """Search for tickers matching the query."""
    df = load_dataframe()
    # Filter rows where Ticker starts with query
    filtered_df = df[df["Ticker"].str.startswith(query, na=False)]
    # Get just the Ticker column
    ticker_series = filtered_df["Ticker"]
    # Convert to list and limit results
    matches = ticker_series.tolist()[:limit]
    return matches

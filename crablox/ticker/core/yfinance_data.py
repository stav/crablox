from typing import Dict, Optional, Tuple

import pandas as pd
import yfinance as yf


def fetch_yfinance_data(
    ticker: str,
) -> Tuple[Dict[int, float], Dict[int, Optional[float]], Dict[int, float]]:
    """
    Fetch historical data from yfinance for a given ticker.

    Args:
        ticker: The stock ticker symbol

    Returns:
        Tuple containing:
        - avg_price_by_year: Dictionary mapping years to average stock prices
        - avg_mcap_by_year: Dictionary mapping years to average market caps (can be None)
        - net_income_by_year: Dictionary mapping years to net income values
    """
    try:
        yf_ticker = yf.Ticker(ticker)
        shares_outstanding = yf_ticker.info.get("sharesOutstanding")

        # Fetch historical price data
        hist = yf_ticker.history(period="5y")
        hist.index = pd.to_datetime(hist.index)
        hist["Year"] = hist.index.year
        avg_price_by_year = (
            hist.groupby("Year")["Close"].mean().to_dict() if not hist.empty else {}
        )

        # Calculate market cap by year
        avg_mcap_by_year = {
            year: (
                (avg_price_by_year[year] * shares_outstanding)
                if shares_outstanding
                else None
            )
            for year in avg_price_by_year
        }

        # Fetch Net Income from yfinance financials
        fin = yf_ticker.financials
        net_income_by_year = {}
        if not fin.empty and "Net Income" in fin.index:
            for col in fin.columns:
                try:
                    year = int(str(col)[:4])
                    net_income = fin.at["Net Income", col]
                    if net_income not in (None, 0):
                        net_income_by_year[year] = net_income
                except Exception:
                    continue

        return avg_price_by_year, avg_mcap_by_year, net_income_by_year

    except Exception:
        return {}, {}, {}

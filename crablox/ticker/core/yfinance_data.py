from typing import Dict, Optional, Tuple

import pandas as pd
import yfinance as yf


def fetch_yfinance_data(
    ticker: str,
) -> Tuple[Dict[int, float], Dict[int, Optional[float]], Dict[int, float], Dict[int, float], Dict[int, float], str]:
    """
    Fetch historical data from yfinance for a given ticker.

    Shares information:

        yf_ticker.info <dict>
            'floatShares':              904509734,
            'impliedSharesOutstanding': 907139968,
            'sharesOutstanding':        907139968,
            'revenuePerShare': 446.442,

        yf_ticker.financials <DataFrame>
                                    2024-12-31  2023-12-31  2022-12-31  2021-12-31
            Diluted Average Shares   929000000   938000000   950000000   956000000
            Basic Average Shares     915000000   924000000   934000000   943000000

        yf_ticker.balance_sheet <DataFrame>
                                    2024-12-31  2023-12-31  2022-12-31  2021-12-31
            Ordinary Shares Number   915000000   924000000   934000000   941000000
            Share Issued             915000000   924000000   934000000   941000000

    Args:
        ticker: The stock ticker symbol

    Returns:
        Tuple containing:
        - avg_price_by_year: Dictionary mapping years to average stock prices
        - avg_mcap_by_year: Dictionary mapping years to average market caps (can be None)
        - net_income_by_year: Dictionary mapping years to net income values
        - revenue_by_year: Dictionary mapping years to revenue values
        - shares_by_year: Dictionary mapping years to shares outstanding values
        - company_name: The company's long name from Yahoo Finance
    """
    try:
        yf_ticker = yf.Ticker(ticker)

        shares_outstanding = yf_ticker.info.get("sharesOutstanding")
        company_name = yf_ticker.info.get("longName", ticker)

        # Fetch historical price data
        hist = yf_ticker.history(period="5y")
        hist.index = pd.to_datetime(hist.index)
        hist["Year"] = hist.index.year
        avg_price_by_year = (
            hist.groupby("Year")["Close"].mean().to_dict() if not hist.empty else {}
        )

        # Fetch financial data
        fin = yf_ticker.financials
        net_income_by_year = {}
        revenue_by_year = {}
        shares_by_year = {}
        if not fin.empty:
            # Get Net Income
            if "Net Income" in fin.index:
                for col in fin.columns:
                    try:
                        year = int(str(col)[:4])
                        net_income = fin.at["Net Income", col]
                        if net_income not in (None, 0):
                            net_income_by_year[year] = net_income
                    except Exception:
                        continue
            
            # Get Revenue
            if "Total Revenue" in fin.index:
                for col in fin.columns:
                    try:
                        year = int(str(col)[:4])
                        revenue = fin.at["Total Revenue", col]
                        if revenue not in (None, 0):
                            revenue_by_year[year] = revenue
                    except Exception:
                        continue

            # Get Shares Outstanding from balance sheet
            bs = yf_ticker.balance_sheet
            if not bs.empty and "Share Issued" in bs.index:
                for col in bs.columns:
                    try:
                        year = int(str(col)[:4])
                        shares = bs.at["Share Issued", col]
                        if shares not in (None, 0):
                            shares_by_year[year] = shares
                    except Exception:
                        continue

        # Fill in missing years with current shares outstanding
        for year in avg_price_by_year:
            if year not in shares_by_year and shares_outstanding:
                shares_by_year[year] = shares_outstanding

        # Calculate market cap by year using historical shares data
        avg_mcap_by_year = {
            year: (
                (avg_price_by_year[year] * shares_by_year[year])
                if year in shares_by_year and shares_by_year[year]
                else None
            )
            for year in avg_price_by_year
        }

        return avg_price_by_year, avg_mcap_by_year, net_income_by_year, revenue_by_year, shares_by_year, company_name

    except Exception:
        return {}, {}, {}, {}, {}, ticker

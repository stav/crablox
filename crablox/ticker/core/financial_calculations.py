from typing import Dict, Optional, List, Tuple


def calculate_eps(
    net_income_by_year: Dict[int, float],
    shares_by_year: Dict[int, float],
    years: List[int]
) -> Dict[int, Optional[float]]:
    """Calculate EPS for all years using historical shares outstanding."""
    eps_by_year: Dict[int, Optional[float]] = {}
    for year in years:
        net_income = net_income_by_year.get(year)
        shares = shares_by_year.get(year)
        if net_income is not None and shares is not None and shares != 0:
            eps_by_year[year] = net_income / shares
        else:
            eps_by_year[year] = None
    return eps_by_year


def calculate_earnings_growth(
    eps_by_year: Dict[int, Optional[float]],
    years: List[int]
) -> Dict[int, Optional[float]]:
    """Calculate earnings growth rate year over year."""
    earnings_growth_by_year: Dict[int, Optional[float]] = {}
    for i, year in enumerate(years[1:], 1):
        prev_year = years[i - 1]
        prev_eps = eps_by_year.get(prev_year)
        curr_eps = eps_by_year.get(year)
        if prev_eps is not None and curr_eps is not None and prev_eps != 0:
            earnings_growth_by_year[year] = (curr_eps - prev_eps) / abs(prev_eps)
        else:
            earnings_growth_by_year[year] = None
    return earnings_growth_by_year


def calculate_pe_ratio(
    avg_price_by_year: Dict[int, float],
    eps_by_year: Dict[int, Optional[float]],
    years: List[int]
) -> Dict[int, Optional[float]]:
    """Calculate PE ratio for each year."""
    pe_by_year: Dict[int, Optional[float]] = {}
    for year in years:
        price = avg_price_by_year.get(year)
        eps = eps_by_year.get(year)
        if price is not None and eps is not None and eps != 0:
            pe_by_year[year] = price / eps
        else:
            pe_by_year[year] = None
    return pe_by_year


def calculate_peg_ratio(
    pe_by_year: Dict[int, Optional[float]],
    earnings_growth_by_year: Dict[int, Optional[float]],
    years: List[int]
) -> Dict[int, Optional[float]]:
    """Calculate PEG ratio for each year."""
    peg_by_year: Dict[int, Optional[float]] = {}
    for year in years:
        pe = pe_by_year.get(year)
        growth = earnings_growth_by_year.get(year)
        if pe is not None and growth is not None and growth != 0:
            peg_by_year[year] = pe / (growth * 100)
        else:
            peg_by_year[year] = None
    return peg_by_year


def calculate_revenue_growth(
    revenue_by_year: Dict[int, float],
    years: List[int]
) -> Dict[int, Optional[float]]:
    """Calculate revenue growth rate year over year."""
    revenue_growth_by_year: Dict[int, Optional[float]] = {}
    for i, year in enumerate(years[1:], 1):
        prev_year = years[i - 1]
        prev_revenue = revenue_by_year.get(prev_year)
        curr_revenue = revenue_by_year.get(year)
        if prev_revenue is not None and curr_revenue is not None and prev_revenue != 0:
            revenue_growth_by_year[year] = (curr_revenue - prev_revenue) / prev_revenue
        else:
            revenue_growth_by_year[year] = None
    return revenue_growth_by_year


def calculate_revenue_multiple(
    avg_mcap_by_year: Dict[int, Optional[float]],
    revenue_by_year: Dict[int, float],
    years: List[int]
) -> Dict[int, Optional[float]]:
    """Calculate revenue multiple (Price/Sales) for each year."""
    revenue_multiple_by_year: Dict[int, Optional[float]] = {}
    for year in years:
        mcap = avg_mcap_by_year.get(year)
        revenue = revenue_by_year.get(year)
        if mcap is not None and revenue is not None and revenue != 0:
            revenue_multiple_by_year[year] = mcap / revenue
        else:
            revenue_multiple_by_year[year] = None
    return revenue_multiple_by_year


def get_year_suffixes(current_year: int) -> Dict[int, List[str]]:
    """Get the mapping of years to their fiscal year suffixes."""
    return {
        current_year - 2: ["FY-1"],
        current_year - 1: ["FY0", "F0"],
        current_year + 0: ["FY1", "F1"],
        current_year + 1: ["FY2", "F2"],
        current_year + 2: ["FY3", "F3"],
    } 
